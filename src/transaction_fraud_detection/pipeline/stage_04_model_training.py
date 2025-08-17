from src.transaction_fraud_detection.logging import logger 
from src.transaction_fraud_detection.config.configuration import ConfigManager
from src.transaction_fraud_detection.components.model_training import ModelTraining

stage_four="Model Training"

class ModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config=ConfigManager()
        model_training_config=config.get_model_trainer_config()
        model_training=ModelTraining(config=model_training_config)
        model_training.model_training()


if __name__=="__main__":
    try: 
        logger.info(f"<<<< stage: {stage_four} started")
        obj=ModelTrainingPipeline()
        obj.main()
        logger.info(f"stage: {stage_four} completed >>>>")
    except Exception as e: 
        logger.info(e)
        raise e

