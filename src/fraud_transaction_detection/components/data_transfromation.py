import os
import joblib
import pandas as pd 
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import SMOTE
from sklearn.model_selection import train_test_split
from src.fraud_transaction_detection.logging import logger
from src.fraud_transaction_detection.entity.config_entity import DataTransformationConfig



"""DataTransformation class contain method that preprocess data(drop irrelavent columns),
 encode categorical data,oversampling,scale,split data into train an test"""
class DataTransformation:
    def __init__(self,config:DataTransformationConfig):
        self.config=config 
        self.encode_Transaction_Type=OneHotEncoder(sparse_output=False)
        self.encode_Device_Type=OneHotEncoder(sparse_output=False)
        self.encode_Card_Type=OneHotEncoder(sparse_output=False) 
        self.scale=StandardScaler()
        self.sampling=SMOTE()
    
    # method to preprocess data
    def data_preprocessing(self):
        data=pd.read_csv(self.config.data_path)
        data.drop(["Transaction_ID","User_ID","Timestamp","Merchant_Category","Authentication_Method","Location","Daily_Transaction_Count","Previous_Fraudulent_Activity","IP_Address_Flag","Card_Age","Is_Weekend","Avg_Transaction_Amount_7d","Account_Balance","Transaction_Distance","Transaction_Amount"],axis=1,inplace=True)
        return data 
    
    # method for encode categorical data to numerical by using onehotencoding
    def encoding(self):
        data=self.data_preprocessing()
        data=pd.concat([data.drop(["Transaction_Type"],axis=1),pd.DataFrame(self.encode_Transaction_Type.fit_transform(data[["Transaction_Type"]]),columns=self.encode_Transaction_Type.get_feature_names_out())],axis=1)
        data=pd.concat([data.drop(["Device_Type"],axis=1),pd.DataFrame(self.encode_Device_Type.fit_transform(data[["Device_Type"]]),columns=self.encode_Device_Type.get_feature_names_out())],axis=1)
        data=pd.concat([data.drop(["Card_Type"],axis=1),pd.DataFrame(self.encode_Card_Type.fit_transform(data[["Card_Type"]]),columns=self.encode_Card_Type.get_feature_names_out())],axis=1)
        joblib.dump(self.encode_Transaction_Type,(self.config.root_dir,"encode_Transaction_Type.joblib"))
        joblib.dump(self.encode_Device_Type,os.path.join(self.config.root_dir,"encode_Device_Type.joblib"))
        joblib.dump(self.encode_Card_Type,os.path.join(self.config.root_dir,"encode_Card_Type.joblib"))
        return data
    
    # method to perform oversampling, scale and split data into train and test
    def oversampling_scaling_split(self):
        try:
            data=self.encoding()

            #divide data into input and target column
            x=data.drop([self.config.target_col],axis=1)
            y=data[self.config.target_col]

            train_x,test_x,train_y,test_y=train_test_split(x,y,test_size=0.2,random_state=42)

            # oversampling for imbalanced dataset
            sampled_train_x,sampled_train_y=self.sampling.fit_resample(train_x,train_y)

            #scale data by using StandardScaler
            scale_train_x=self.scale.fit_transform(sampled_train_x)
            scale_test_x=self.scale.transform(test_x)
            joblib.dump(self.scale,os.path.join(self.config.root_dir,"scale.joblib"))
            
            train_data=pd.concat([pd.DataFrame(scale_train_x).reset_index(drop=True),sampled_train_y.reset_index(drop=True)],axis=1)
            test_data=pd.concat([pd.DataFrame(scale_test_x).reset_index(drop=True),test_y],axis=1)

            # saved split data to defined path 
            train_data.to_csv(os.path.join(self.config.root_dir,"train_data.csv"),index=False)
            test_data.to_csv(os.path.join(self.config.root_dir,"test_data.csv"),index=False)

            logger.info("data split sucessfully")
            logger.info(f"train data shape: {train_data.shape}")
            logger.info(f"test data shape: {test_data.shape}")

        except Exception as e:
            raise e




