from src.fraud_transaction_detection.config.configuration import ConfigManager 
from src.fraud_transaction_detection.components.model_trainer import ModelTrainer


"""
ModelTrainerPipeline class is pipeline to train model and save at defined path
"""
class ModelTrainerPipeline:
    def __init__(self):
        pass

    def main(self):
        config=ConfigManager()                                         # create object of configmanager      
        model_trainer_config=config.get_model_trainer_config()         # get model trainer config
        model_trainer=ModelTrainer(config=model_trainer_config)        # create object of model trainer
        model_trainer.train_model()                                    # train model with train data
