import os
import joblib
import pandas as pd 
import numpy as np
from pathlib import Path
from sklearn.metrics import accuracy_score,confusion_matrix,precision_score,recall_score,f1_score,roc_auc_score
from src.fraud_transaction_detection.utils.common import save_json
from src.fraud_transaction_detection.entity.config_entity import ModelEvaluationConfig



"""ModelEvaluation class contain method of evaluation in which it will 
return evaluation metrics for classification """
class ModelEvaluation:
    def __init__(self,config:ModelEvaluationConfig):
        self.config=config 
        self.model=joblib.load(self.config.model_path)
    
    # method to get metrics for classification
    def get_metrics(self,actual,predicted):
        acc=accuracy_score(actual,predicted)
        cf=confusion_matrix(actual,predicted)
        pr=precision_score(actual,predicted)
        rc=recall_score(actual,predicted)
        f1=f1_score(actual,predicted)
        roc=roc_auc_score(actual,predicted)
        return acc,cf,pr,rc,f1,roc
    
    # method to evaluate model on test data and save metrics score
    def evaluation(self):
        try:
            # read test data
            data=pd.read_csv(self.config.test_data)           

            # split data into input and target column
            test_x=data.drop([self.config.target_col],axis=1)  
            test_y=data[self.config.target_col]

            # make prediction on test data
            prediction=self.model.predict(test_x)

            # get metrics score for test data
            (acc,cf,pr,rc,f1,roc)=self.get_metrics(test_y,prediction)

            # create dict of metrics
            scores={"accuracy score":acc,"confusion matrix":cf.tolist(),"precision score":pr,"recall score":rc,"f1-score":f1,"roc auc score":roc}

            # save metrics as json file to defined path
            save_json(Path(self.config.metrics_file),scores)
        
        except Exception as e:
            raise e
