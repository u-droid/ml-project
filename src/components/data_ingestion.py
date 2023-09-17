import os
import sys
import pandas as pd
from src.exception import CustomException
from src.logger import logging
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer

@dataclass
class DataIngestionConfig:
    train_data_path = os.path.join('artifacts', 'train.csv')
    test_data_path = os.path.join('artifacts','test.csv')
    raw_data_path = os.path.join('artifacts','data.csv')

class DataIngestion:
    def __init__(self) -> None:
        self.ingestion_config = DataIngestionConfig()
    
    def initiate_data_ingestion(self):
        logging.info('Entered Data Ingestion')
        try:
            df = pd.read_csv('notebook/data/stud.csv')
            logging.info('Read the data as dataframe')
            os.makedirs( os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path, header=True, index=False)
            
            logging.info('Train Test Split Initiated')
            train, test = train_test_split(df, test_size=0.2, random_state=42)
            train.to_csv(self.ingestion_config.train_data_path, header=True, index=False)
            test.to_csv(self.ingestion_config.test_data_path, header=True, index=False)
            logging.info('Ingestion of data is completed')
            return self.ingestion_config.train_data_path, self.ingestion_config.test_data_path
        except Exception as e:
            raise CustomException(e, sys)

if __name__ == '__main__':
    ingestion = DataIngestion()
    train_path, test_path = ingestion.initiate_data_ingestion()

    data_prep = DataTransformation()
    train, test, preprocessor_obj_file_path = data_prep.initiate_data_transformation(train_path, test_path)

    trainer = ModelTrainer()
    best_model_score = trainer.initiate_model_trainer()
    print(f"Best Model R2 Score= {best_model_score}")



