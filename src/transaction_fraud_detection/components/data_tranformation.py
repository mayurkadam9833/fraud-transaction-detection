import os
import pandas as pd
import joblib
from src.transaction_fraud_detection.logging import logger
from src.transaction_fraud_detection.config.configuration import ConfigManager
from src.transaction_fraud_detection.entity.config_entity import DataTransformationConfig
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import SMOTE

class DataTranformation:
    def __init__(self,config:DataTransformationConfig):
        self.config=config
        self.encode=OneHotEncoder(sparse_output=False)
        self.sampling=SMOTE()
        self.scale=StandardScaler()
        


    def drop_columns(self):
        data=pd.read_csv(self.config.data_path)

        data.drop(["nameOrig","nameDest"],axis=1,inplace=True)

        return data
    
    def encode_feature(self):
        data=self.drop_columns()
        encode_data=pd.DataFrame(self.encode.fit_transform(data[["type"]]),columns=self.encode.get_feature_names_out())
        data=pd.concat([data.drop(["type"],axis=1),encode_data],axis=1)
        joblib.dump(self.encode,os.path.join(self.config.root_dir,"encode.joblib"))
        return data
    
    def split_data(self):
        try:
            data=self.encode_feature()

            x=data.drop(["isFraud"],axis=1)
            y=data["isFraud"]

            train_x,test_x,train_y,test_y=train_test_split(x,y,test_size=0.3,random_state=42)

            sample_train_x,sample_train_y=self.sampling.fit_resample(train_x,train_y)
            scale_train_x=self.scale.fit_transform(sample_train_x)
            scale_test_x=self.scale.transform(test_x)
            joblib.dump(self.scale,os.path.join(self.config.root_dir,"scale.joblib"))

            train_data = pd.concat([pd.DataFrame(scale_train_x).reset_index(drop=True),pd.Series(sample_train_y).reset_index(drop=True)],axis=1)
            test_data=pd.concat([pd.DataFrame(scale_test_x).reset_index(drop=True),pd.Series(test_y).reset_index(drop=True)],axis=1)

            train_data.to_csv(os.path.join(self.config.root_dir,"train.csv"),index=False)
            test_data.to_csv(os.path.join(self.config.root_dir,"test.csv"),index=False)
            
            logger.info("train test split scuessfully")
            logger.info(train_data.shape)
            logger.info(test_data.shape)

        except Exception as e:
            raise e

            



