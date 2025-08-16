from src.transaction_fraud_detection.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from src.transaction_fraud_detection.pipeline.stage_02_data_validation import DataValidationPipeline
from src.transaction_fraud_detection.pipeline.stage_03_data_transformation import DataTransformationPipeline
from src.transaction_fraud_detection.logging import logger

stage_one="Data Ingestion"

if __name__ == "__main__":
    try:
        logger.info(f"<<<< stage: {stage_one} started")
        obj=DataIngestionPipeline()
        obj.main()
        logger.info(f"stage: {stage_one} completed >>>>")
    except Exception as e:
        logger.info(e)
        raise e

stage_two="data validation"

if __name__ == "__main__":
    try:
        logger.info(f"<<<< stage: {stage_two} started")
        obj=DataValidationPipeline()
        obj.main()
        logger.info(f"stage: {stage_two} completed >>>>")
    except Exception as e:
        logger.info(e)
        raise e
    
stage_three="Data Transformation"

if __name__ == "__main__":
    try:
        logger.info(f"<<<< stage: {stage_three} started")
        obj=DataTransformationPipeline()
        obj.main()
        logger.info(f"<<<< stage: {stage_three} started")
    except Exception as e:
        logger.info(e)
        raise e