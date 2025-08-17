import joblib
import pandas as pd 
import numpy as np 
from pathlib import Path

class PredictionPipeline:
    def __init__(self):
        self.encode=joblib.load(Path("artifacts/data_transformation/encode.joblib"))
        self.scale=joblib.load(Path("artifacts/data_transformation/scale.joblib"))
        self.model=joblib.load(Path("artifacts/model_trainer/model.joblib"))

    def preprocess(self,data:pd.DataFrame):
        data=data.drop(["nameOrig", "nameDest"],axis=1,errors="ignore")

        encoded=pd.DataFrame(
            self.encode.transform(data[["type"]]),
            columns=self.encode.get_feature_names_out(),
            index=data.index
        )
        
        data=pd.concat([data.drop(["type"],axis=1),encoded],axis=1)

        scaled=self.scale.transform(data)
        return scaled
    
    def predict(self,data:pd.DataFrame):
        processed=self.preprocess(data)
        prediction=self.model.predict(processed)
        return prediction
    
    def predict_proba(self, data: pd.DataFrame):
        processed = self.preprocess(data)
        probs = self.model.predict_proba(processed)
        return probs[0][1]