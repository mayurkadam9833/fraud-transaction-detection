from src.transaction_fraud_detection.config.configuration import ConfigManager 
from src.transaction_fraud_detection.components.model_evaluation import ModelEvaluation
from src.transaction_fraud_detection.logging import logger

stage_five="Model Evaluation"

class ModelEvaluationPipeline: 
    def __init__(self):
        pass

    def main(self): 
        config=ConfigManager()
        model_evaluation_config=config.get_model_evaluation_config()
        model_evalution=ModelEvaluation(config=model_evaluation_config)
        model_evalution.save_result()

if __name__ == "__main__":
    try:
        logger.info(f"<<<< stage: {stage_five} started")
        obj=ModelEvaluationPipeline()
        obj.main()
        logger.info(f"stage: {stage_five} completed >>>>")
    except Exception as e: 
        logger.info(e)
        raise e
