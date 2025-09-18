from src.fraud_transaction_detection.config.configuration import ConfigManager
from src.fraud_transaction_detection.components.data_validation import DataValidation


"""
DataValidationPipeline class is pipeline to validate schema of data with defined schema
"""
class DataValidationPipeline:
    def __init__(self):
        pass

    def main(self):
        config=ConfigManager()                                          # create object of configmanager
        data_validation_config=config.get_data_validation_config()      # get data validation config 
        data_validation=DataValidation(config=data_validation_config)   # create object of data validation
        data_validation.schema_validation()                             # data validation 