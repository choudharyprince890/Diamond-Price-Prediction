import os 
import sys
from src.logger import logging
from src.exception import CustomException
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass  # used to create variable directly in the class


# Intitialize the Data Ingetion Configuration
@dataclass
class DataIngestionconfig:
    train_data_path:str=os.path.join('artifacts','train.csv')
    test_data_path:str=os.path.join('artifacts','test.csv')
    raw_data_path:str=os.path.join('artifacts','raw.csv')

# createaclass for data ingestion
class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionconfig

    def intitate_data_ingestion(self):
        logging.info("Data Ingestion Starts")
        try:
            df = pd.read_csv(os.path.join('notebook/data','gemstone.csv'))
            logging.info("Dataset read as pandas dataframe")

            os.mkdir(os.path.dirname(self.ingestion_config.raw_data_path),exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path,index=False)
            logging.info('Train Test Split')

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info('Ingestion Data is completed')

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        
        except Exception as e:
            logging.info('Exception occoured at Data Ingestion stage')
            raise CustomException(e,sys)


