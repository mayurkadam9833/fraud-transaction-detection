import pandas as pd
import numpy as np 
import joblib 
from pathlib import Path
from src.transaction_fraud_detection.utils.common import save_json
from sklearn.metrics import accuracy_score,confusion_matrix,precision_score,recall_score,f1_score,roc_auc_score
from src.transaction_fraud_detection.entity.config_entity import ModelEvaluationConfig
from src.transaction_fraud_detection.config.configuration import ConfigManager


class ModelEvaluation:
    def __init__(self,config:ModelEvaluationConfig):
        self.config=config 

    def get_metrics(self,actual,predicted):
        acc=accuracy_score(actual,predicted)
        cf=confusion_matrix(actual,predicted)
        pr=precision_score(actual,predicted)
        rc=recall_score(actual,predicted)
        f1=f1_score(actual,predicted)
        roc=roc_auc_score(actual,predicted)
        return acc,cf,pr,rc,f1,roc

    def save_result(self):
        test_data=pd.read_csv(self.config.test_data_path)
        model=joblib.load(self.config.model_path)

        test_x=test_data.drop([self.config.target_column],axis=1)
        test_y=test_data[[self.config.target_column]]

        prediction=model.predict(test_x)

        (acc,cf,pr,rc,f1,roc)=self.get_metrics(test_y,prediction)

        scores={"accuracy score":acc,"confusion matix":cf.tolist(),"precision score":pr,"recall score":rc,"f1-score":f1,"roc auc score":roc}
        save_json(path=Path(self.config.metric_file_name),data=scores)

