from src.fraud_transaction_detection.config.configuration import ConfigManager
from src.fraud_transaction_detection.components.data_ingestion import DataIngestion


"""
DataIngestionPipeline class is pipeline to download file and extract file in define folder
"""
class DataIngestionPipeline:
    def __init__(self):
        pass
    def main(self):
        config=ConfigManager()                                         # create object of configmanager
        data_ingsetion_config=config.get_data_ingestion_config()       # get data ingsetion config
        data_insgetion=DataIngestion(config=data_ingsetion_config)     # craete object of DataIngestion
        data_insgetion.download_file()                                 # download data file                        
        data_insgetion.extract_file()                                  # extract zip file
