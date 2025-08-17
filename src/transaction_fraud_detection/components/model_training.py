import os
import pandas as pd 
import joblib
from xgboost import XGBClassifier 
from src.transaction_fraud_detection.entity.config_entity import ModelTrainerConfig

class ModelTraining:
    def __init__(self,config:ModelTrainerConfig):
        self.config=config

    def model_training(self):
            train_data=pd.read_csv(self.config.train_data_path)
            test_data=pd.read_csv(self.config.test_data_path)

            train_x=train_data.drop([self.config.target_column],axis=1)
            train_y=train_data[[self.config.target_column]]
            test_x=test_data.drop([self.config.target_column],axis=1)
            test_y=test_data[[self.config.target_column]]

            xgb=XGBClassifier( subsample=0.8,reg_lambda=1,reg_alpha=0.1,n_estimators=150,min_child_weight=1,max_depth=30,learning_rate=0.02,colsample_bytree=0.6)

            xgb.fit(train_x,train_y)

            joblib.dump(xgb,os.path.join(self.config.root_dir,self.config.model_name))