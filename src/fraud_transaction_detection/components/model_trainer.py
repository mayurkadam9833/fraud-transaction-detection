import os
import joblib
import pandas as pd 
from sklearn.svm import SVC
from src.fraud_transaction_detection.entity.config_entity import ModelTrainerConfig
from src.fraud_transaction_detection.logging import logger


"""ModelTrainer class contain method of train_model
which train model with train dataset and save train model to defined path"""
class ModelTrainer:
    def __init__(self,config:ModelTrainerConfig):
        self.config=config
        self.model=SVC(kernel=self.config.kernel,degree=self.config.degree)

    # method to train model
    def train_model(self):
        try:
            # read train data
            data=pd.read_csv(self.config.train_data)

            # split into input and target column
            train_x=data.drop([self.config.target_col],axis=1)
            train_y=data[self.config.target_col]

            # train model
            model=self.model.fit(train_x,train_y)

            # save model at defined path
            model_path=os.path.join(self.config.root_dir,"model.joblib")
            joblib.dump(model,model_path)

            logger.info(f"model train sucessfully")

        except Exception as e:
            raise e