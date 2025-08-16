from src.transaction_fraud_detection.logging import logger
from src.transaction_fraud_detection.config.configuration import ConfigManager
from src.transaction_fraud_detection.components.data_tranformation import DataTranformation

stage_three="Data Transformation"

class DataTransformationPipeline:
    def __init__(self):
        pass

    def main(self):
        config=ConfigManager()
        data_transformation_config=config.get_data_tranformation_config()
        data_transformation=DataTranformation(config=data_transformation_config)
        data_transformation.drop_columns()
        data_transformation.encode_feature()
        data_transformation.split_data()



if __name__ == "__main__":
    try:
        logger.info(f"<<<< stage: {stage_three} started")
        obj=DataTransformationPipeline()
        obj.main()
        logger.info(f"<<<< stage: {stage_three} started")
    except Exception as e:
        logger.info(e)
        raise e