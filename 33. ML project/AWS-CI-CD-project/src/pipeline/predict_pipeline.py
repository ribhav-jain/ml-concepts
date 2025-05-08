import sys
import pandas as pd
from src.exception import CustomException
from src.utils import load_object
import os


class PredictPipeline:
    """
    Class to handle the loading of the model and preprocessor,
    data scaling, and making predictions.
    """

    def __init__(self):
        pass

    def predict(self, features: pd.DataFrame):
        """
        Predict the target variable based on the input features.

        Parameters:
        - features: Input data to make predictions.

        Returns:
        - preds: Predicted values after model inference.
        """
        try:
            # Define paths for model and preprocessor
            model_path = os.path.join("artifacts", "model.pkl")
            preprocessor_path = os.path.join("artifacts", "preprocessor.pkl")

            # Load model and preprocessor
            model = load_object(file_path=model_path)
            preprocessor = load_object(file_path=preprocessor_path)

            # Scale the input data using the preprocessor
            data_scaled = preprocessor.transform(features)

            # Make predictions using the trained model
            preds = model.predict(data_scaled)
            return preds

        except Exception as e:
            raise CustomException(f"Error in prediction pipeline: {e}", sys)


class CustomData:
    """
    Custom data class to store user input features and convert them into
    a structured pandas DataFrame for predictions.
    """

    def __init__(
        self,
        gender: str,
        race_ethnicity: str,
        parental_level_of_education: str,
        lunch: str,
        test_preparation_course: str,
        reading_score: int,
        writing_score: int,
    ):
        """
        Initializes the input features for the prediction pipeline.
        """
        self.gender = gender
        self.race_ethnicity = race_ethnicity
        self.parental_level_of_education = parental_level_of_education
        self.lunch = lunch
        self.test_preparation_course = test_preparation_course
        self.reading_score = reading_score
        self.writing_score = writing_score

    def get_data_as_data_frame(self) -> pd.DataFrame:
        """
        Converts the input features into a pandas DataFrame for predictions.

        Returns:
        - DataFrame: A DataFrame containing all user input features.
        """
        try:
            # Create a dictionary from the input features
            custom_data_input_dict = {
                "gender": [self.gender],
                "race_ethnicity": [self.race_ethnicity],
                "parental_level_of_education": [self.parental_level_of_education],
                "lunch": [self.lunch],
                "test_preparation_course": [self.test_preparation_course],
                "reading_score": [self.reading_score],
                "writing_score": [self.writing_score],
            }

            # Return the dictionary as a pandas DataFrame
            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise CustomException(f"Error in converting data to DataFrame: {e}", sys)
