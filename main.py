from src.fraud_transaction_detection.logging import logger
from src.fraud_transaction_detection.pipeline.stage_01_data_ingestion_pipeline import DataIngestionPipeline



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