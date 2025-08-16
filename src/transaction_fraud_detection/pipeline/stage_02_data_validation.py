from src.transaction_fraud_detection.components.data_validation import DataValidation
from src.transaction_fraud_detection.config.configuration import ConfigManager
from src.transaction_fraud_detection.logging import logger


stage_two="data validation"


class DataValidationPipeline:
    def __init__(self):
        pass

    def main(self):
        config=ConfigManager()
        data_validation_config=config.get_data_validation_config()
        data_validation=DataValidation(config=data_validation_config)
        data_validation.schema_validation()
        data_validation.data_type_validation()

if __name__ == "__main__":
    try:
        logger.info(f"<<<< stage: {stage_two} started")
        obj=DataValidationPipeline()
        obj.main()
        logger.info(f"stage: {stage_two} completed >>>>")
    except Exception as e:
        logger.info(e)
        raise e