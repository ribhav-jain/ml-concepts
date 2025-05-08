import os
import sys
from dataclasses import dataclass  # Importing the dataclass decorator

from catboost import CatBoostRegressor
from sklearn.ensemble import (
    AdaBoostRegressor,
    GradientBoostingRegressor,
    RandomForestRegressor,
)
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor

from src.exception import CustomException
from src.logger import logging
from src.utils import save_object, evaluate_models


@dataclass
class ModelTrainerConfig:
    """
    Configuration class to store model file paths.
    The `@dataclass` decorator automatically adds special methods to the class
    like __init__, __repr__, and __eq__.

    This is used for simple classes to hold configuration data without needing
    to manually write these methods. Here, we use it to store the file path
    for the trained model that will be saved after training.
    """

    trained_model_file_path = os.path.join("artifacts", "model.pkl")


class ModelTrainer:
    """
    Class to train multiple models, evaluate their performance,
    and save the best model.
    """

    def __init__(self):
        """
        Initializes the ModelTrainer with the configuration for saving the trained model.
        The configuration is obtained from the ModelTrainerConfig dataclass.
        """
        self.model_trainer_config = ModelTrainerConfig()

    def initiate_model_trainer(self, train_array, test_array):
        """
        This method trains multiple models and evaluates their performance.
        The best performing model is selected and saved.

        Parameters:
        - train_array: Training dataset (features + target)
        - test_array: Testing dataset (features + target)

        Returns:
        - r2_square: R2 score of the best model on the test set
        """
        try:
            # Log the start of model training
            logging.info("Starting the model training process")

            # Split features and target from the training and testing data
            X_train, y_train, X_test, y_test = (
                train_array[:, :-1],
                train_array[:, -1],
                test_array[:, :-1],
                test_array[:, -1],
            )

            # Define a dictionary of models to train
            models = {
                "Random Forest": RandomForestRegressor(),
                "Decision Tree": DecisionTreeRegressor(),
                "Gradient Boosting": GradientBoostingRegressor(),
                "Linear Regression": LinearRegression(),
                "XGBRegressor": XGBRegressor(),
                "CatBoosting Regressor": CatBoostRegressor(verbose=False),
                "AdaBoost Regressor": AdaBoostRegressor(),
            }

            # Define hyperparameters for each model to be tuned
            params = {
                "Decision Tree": {
                    "criterion": [
                        "squared_error",
                        "friedman_mse",
                        "absolute_error",
                        "poisson",
                    ],
                },
                "Random Forest": {"n_estimators": [8, 16, 32, 64, 128, 256]},
                "Gradient Boosting": {
                    "learning_rate": [0.1, 0.01, 0.05, 0.001],
                    "subsample": [0.6, 0.7, 0.75, 0.8, 0.85, 0.9],
                    "n_estimators": [8, 16, 32, 64, 128, 256],
                },
                "Linear Regression": {},
                "XGBRegressor": {
                    "learning_rate": [0.1, 0.01, 0.05, 0.001],
                    "n_estimators": [8, 16, 32, 64, 128, 256],
                },
                "CatBoosting Regressor": {
                    "depth": [6, 8, 10],
                    "learning_rate": [0.01, 0.05, 0.1],
                    "iterations": [30, 50, 100],
                },
                "AdaBoost Regressor": {
                    "learning_rate": [0.1, 0.01, 0.5, 0.001],
                    "n_estimators": [8, 16, 32, 64, 128, 256],
                },
            }

            # Evaluate all models using cross-validation and grid search
            model_report: dict = evaluate_models(
                X_train=X_train,
                y_train=y_train,
                X_test=X_test,
                y_test=y_test,
                models=models,
                param=params,
            )

            # Identify the best model based on the highest R2 score
            best_model_score = max(sorted(model_report.values()))
            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]
            best_model = models[best_model_name]

            # Log the best model's name and score
            logging.info(
                f"Best model: {best_model_name} with R2 score: {best_model_score}"
            )

            # If the best model score is less than threshold, raise an exception
            if best_model_score < 0.6:
                raise CustomException("No model achieved a satisfactory performance")

            # Save the best model for future use
            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj=best_model,
            )

            # Predict using the best model and evaluate the performance
            predicted = best_model.predict(X_test)
            r2_square = r2_score(y_test, predicted)

            # Return R2 score of the best model on the test set
            return r2_square

        except Exception as e:
            raise CustomException(f"Error in model training process: {e}", sys)
