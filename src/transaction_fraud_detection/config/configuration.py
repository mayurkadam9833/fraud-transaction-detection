from src.transaction_fraud_detection.entity.config_entity import DataIngestionConfig 
from src.transaction_fraud_detection.constants import * 
from src.transaction_fraud_detection.utils.common import read_yaml,create_directories
from pathlib import Path 


class DataIngestionManager: 
    def __init__(
    self,
    config_file=CONFIG_FILE_PATH, 
    schema_file=SCHEMA_FILE_PATH, 
    params_file=PARAM_FILE_PATH):
     create_directories([self.config.artifacts_roots])

     def get_data_ingestion(self)-> DataIngestionConfig: 
        config=self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config=DataIngestionConfig(
           root_dir=config.root_dir, 
           source_url=config.source_url, 
           local_data_file=config.local_data_file, 
           unzip_dir=config.unzip_dir
        )  
        return DataIngestionConfig
    
        