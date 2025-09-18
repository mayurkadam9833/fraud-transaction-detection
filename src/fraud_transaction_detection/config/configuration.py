from src.fraud_transaction_detection.constants import *
from src.fraud_transaction_detection.utils.common import read_yaml,create_dir
from src.fraud_transaction_detection.entity.config_entity import DataIngestionConfig,DataValidationConfig


"""
ConfigManager class is responsible for reading config, schema and params yaml files
and returning dataclass objects for each pipeline stage (ingestion, validation, transformation, training, evaluation)
"""
class ConfigManager:
    def __init__(
        self,
        config_file=CONFIG_FILE_PATH,
        schema_file=SCHEMA_FILE_PATH,
        params_file=PARAMS_FILE_PATH):

        # read all yaml files (config, schema, params)
        self.config=read_yaml(config_file)
        self.schema=read_yaml(schema_file)
        self.params=read_yaml(params_file)

        # create root artifact directory if not exists
        create_dir([self.config.artifacts_root])

    # method to get data ingestion config object
    def get_data_ingestion_config(self)-> DataIngestionConfig:
        config=self.config.data_ingestion 

        # create data ingestion folder
        create_dir([config.root_dir])

        # prepare and return DataIngestionConfig dataclass
        data_ingsetion_config=DataIngestionConfig(
            root_dir=config.root_dir,
            source_url=config.source_url,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )

        return data_ingsetion_config
    
    # method to get data validation config object
    def get_data_validation_config(self)-> DataValidationConfig:
        config=self.config.data_validation
        schema=self.schema.COLUMNS

        # create data validation folder
        create_dir([config.root_dir])

        # prepare and return DataValidationConfig dataclass
        data_validation_config=DataValidationConfig(
            root_dir=config.root_dir,
            unzip_data=config.unzip_data,
            STATUS_FILE=config.STATUS_FILE,
            all_schema=schema
        )

        return data_validation_config