from src.fraud_transaction_detection.logging import logger
from src.fraud_transaction_detection.pipeline.stage_01_data_ingestion_pipeline import DataIngestionPipeline
from src.fraud_transaction_detection.pipeline.stage_02_data_validation_pipeline import DataValidationPipeline


# data ingestion pipeline execution
stage_one="Data Ingestion"

if __name__ == "__main__":
    try:
        logger.info(f"<<<< stage:{stage_one} started >>>>")
        obj=DataIngestionPipeline()
        obj.main()
        logger.info(f"<<<< stage:{stage_one} completed >>>>")

    except Exception as e:
        logger.info(e)
        raise e

# data validation pipeline execution
stage_two="Data validation"

if __name__ == "__main__":
    try:
        logger.info(f"<<<< stage:{stage_two} started >>>>")
        obj=DataValidationPipeline()
        obj.main()
        logger.info(f"<<<< stage:{stage_two} completed >>>>")

    except Exception as e:
        logger.info(e)
        raise e