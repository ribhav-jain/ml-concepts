import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer


@dataclass
class DataIngestionConfig:
    """
    Holds configuration paths for raw, train, and test data.
    """

    train_data_path: str = os.path.join("artifacts", "train.csv")
    test_data_path: str = os.path.join("artifacts", "test.csv")
    raw_data_path: str = os.path.join("artifacts", "data.csv")


class DataIngestion:
    """
    Handles the ingestion of data, including reading raw data,
    splitting into train and test sets, and saving them to respective paths.
    """

    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        """
        Reads raw data, splits into train and test sets,
        and saves them to the configured paths.
        """
        logging.info("Entered the data ingestion method")
        try:
            # Read the raw dataset
            df = pd.read_csv("notebook/data/stud.csv")
            logging.info("Dataset read into DataFrame")

            # Create directory for storing data if it doesn't exist
            os.makedirs(
                os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True
            )

            # Save raw data
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)
            logging.info(f"Raw data saved to {self.ingestion_config.raw_data_path}")

            # Split data into train and test sets
            logging.info("Train-test split initiated")
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            # Save train and test sets
            train_set.to_csv(
                self.ingestion_config.train_data_path, index=False, header=True
            )
            test_set.to_csv(
                self.ingestion_config.test_data_path, index=False, header=True
            )

            logging.info("Data ingestion completed successfully")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path,
            )
        except Exception as e:
            raise CustomException(f"Error during data ingestion: {e}", sys)


if __name__ == "__main__":
    # Initialize DataIngestion, ingest data, and transform it
    try:
        # Step 1: Data ingestion
        ingestion_obj = DataIngestion()
        train_data, test_data = ingestion_obj.initiate_data_ingestion()

        # Step 2: Data transformation
        data_transformation = DataTransformation()
        train_arr, test_arr, _ = data_transformation.initiate_data_transformation(
            train_data, test_data
        )

        # Step 3: Model training
        model_trainer = ModelTrainer()
        model_score = model_trainer.initiate_model_trainer(train_arr, test_arr)

        logging.info(f"Model training completed with R-squared score: {model_score}")
    except Exception as e:
        logging.error(f"An error occurred during the pipeline execution: {e}")
