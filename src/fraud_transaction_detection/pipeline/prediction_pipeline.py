import joblib
import pandas as pd
from pathlib import Path
from sklearn.preprocessing import OneHotEncoder

"""PredictionPipeline class contain method of preprocessing that encode and scale data and
method of prediction"""
class PredictionPipeline:
    def __init__(self):
        self.self.encode_Transaction_Type=joblib.load(Path("artifacts/data_transformation/encode_Transaction_Type.joblib"))
        self.encode_Device_Type=joblib.load(Path("artifacts/data_transformation/encode_Device_Type.joblib"))
        self.encode_Card_Type=joblib.load(Path("artifacts/data_transformation/encode_Card_Type.joblib"))
        self.scale=joblib.load(Path("artifacts/data_transformation/scale.joblib"))
        self.model=joblib.load(Path("artifacts/data_transformation/model.joblib"))

    # method to preprocess data
    def preprocessing(self,data:pd.DataFrame):
        data=pd.concat([data.drop(["Transaction_Type"],axis=1),pd.DataFrame(self.encode_Transaction_Type.transform(data[["Transaction_Type"]]),columns=self.encode_Transaction_Type.get_feature_names_out())],axis=1)
        data=pd.concat([data.drop(["Device_Type"],axis=1),pd.DataFrame(self.encode_Device_Type.transform(data[["Device_Type"]]),columns=self.encode_Device_Type.get_feature_names_out())],axis=1)
        data=pd.concat([data.drop(["Card_Type"],axis=1),pd.DataFrame(self.encode_Card_Type.transform(data[["Card_Type"]]),columns=self.encode_Card_Type.get_feature_names_out())],axis=1)
        data=self.scale.transform(data)
        return data
    
    # method for prediction
    def prediction(self,data:pd.DataFrame):
        preprocess_data=self.preprocessing()

        prediction=self.model.predict(preprocess_data)

        return prediction

