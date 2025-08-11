from src.transaction_fraud_detection.logging import logger
from src.transaction_fraud_detection.entity.config_entity import DataIngestionConfig
from src.transaction_fraud_detection.config.configuration import ConfigManager
from src.transaction_fraud_detection.components.data_ingestion import DataIngestion


stage_one="Data Ingestion"

class DataIngestionPipeline:
    def __init__(self):
        pass

    def main(self):
        config=ConfigManager()
        data_ingestion_config=config.get_data_ingestion_config()
        data_ingestion=DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_file()


if __name__ == "__main__":
    try:
        logger.info(f"<<<< stage: {stage_one} started")
        obj=DataIngestionPipeline()
        obj.main()
        logger.info(f"stage: {stage_one} completed >>>>")
    except Exception as e:
        logger.info(e)
        raise e
