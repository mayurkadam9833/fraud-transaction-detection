from src.fraud_transaction_detection.constants import *
from src.fraud_transaction_detection.utils.common import read_yaml,create_dir
from src.fraud_transaction_detection.entity.config_entity import DataIngestionConfig,DataValidationConfig,DataTransformationConfig,ModelTrainerConfig,ModelEvaluationConfig


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
    
    # method to get data transformation config object
    def get_data_transformation_config(self)-> DataTransformationConfig:
        config=self.config.data_transformation
        schema=self.schema.TARGET_COLUMN

        # create data transformation folder
        create_dir([config.root_dir])

        # prepare and return DataTransformationConfig dataclass
        data_transformation_config=DataTransformationConfig(
            root_dir=config.root_dir,
            data_path=config.data_path,
            target_col=list(schema.keys())[0]
        )
        return data_transformation_config
    
    # method to get model trainer config object
    def get_model_trainer_config(self)-> ModelTrainerConfig:
        config=self.config.model_trainer
        schema=self.schema.TARGET_COLUMN 
        params=self.params.SVC

        # create model trainer folder
        create_dir([config.root_dir])

        # prepare and return ModelTrainerConfig dataclass
        model_trainer_config=ModelTrainerConfig(
            root_dir=config.root_dir,
            train_data=config.train_data,
            model_name=config.model_name,
            kernel=params.kernel,
            degree=params.degree,
            target_col=list(schema.keys())[0]
        )
        return model_trainer_config
    
    # method to get model evaluation config object
    def get_model_evaluation_config(self)-> ModelEvaluationConfig:
        config=self.config.model_evaluation
        schema=self.schema.TARGET_COLUMN 

        # create model evaluation folder
        create_dir([config.root_dir])

        # prepare and return ModelEvaluationConfig dataclass
        model_evaluation_config=ModelEvaluationConfig(
            root_dir=config.root_dir,
            test_data=config.test_data,
            model_path=config.model_path,
            metrics_file=config.metrics_file,
            target_col=list(schema.keys())[0]
        )
        return model_evaluation_config
