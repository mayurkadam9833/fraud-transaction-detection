import os
import zipfile
from urllib.request import urlretrieve
from src.transaction_fraud_detection.logging import logger
from src.transaction_fraud_detection.entity.config_entity import DataIngestionConfig
from src.transaction_fraud_detection.utils.common import get_size

class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        self.config=config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename,header=urlretrieve(
                url=self.config.source_url,
                filename=self.config.local_data_file
            )
            logger.info(f"{filename} download sucessfully from following header:\n{header}")

        else:
            logger.info(f"file is alreday exists of size:{get_size(self.config.local_data_file)}")

    
    def extract_file(self):
        unzip_path=self.config.unzip_dir
        os.makedirs(unzip_path,exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file,"r")as zipref:
            zipref.extractall(unzip_path)