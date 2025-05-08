import os
import sys
import dill
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV

from src.exception import CustomException


def save_object(file_path, obj):
    """
    Save any Python object to disk using dill.
    """
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)
    except Exception as e:
        raise CustomException(e, sys)


def load_object(file_path):
    """
    Load a Python object from a file using dill.
    """
    try:
        with open(file_path, "rb") as file_obj:
            return dill.load(file_obj)
    except Exception as e:
        raise CustomException(e, sys)


def evaluate_models(
    X_train, y_train, X_test, y_test, models: dict, param: dict
) -> dict:
    """
    Train, tune, and evaluate multiple models. Returns test R² scores.
    """
    try:
        report = {}

        for model_name, model in models.items():
            grid = GridSearchCV(model, param[model_name], cv=3, n_jobs=-1)
            grid.fit(X_train, y_train)

            best_model = grid.best_estimator_
            best_model.fit(X_train, y_train)

            y_test_pred = best_model.predict(X_test)
            test_score = r2_score(y_test, y_test_pred)

            report[model_name] = test_score

        return report
    except Exception as e:
        raise CustomException(e, sys)
