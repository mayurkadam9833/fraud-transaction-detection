import pandas as pd 
from src.fraud_transaction_detection.entity.config_entity import DataValidationConfig


"""
DataValidation class contain method for 
check and validation of schema of dataset with defined schema
"""
class DataValidation:
    def __init__(self,config:DataValidationConfig):
        self.config=config
    
    # method to check if dataset columns match with defined schema columns
    def schema_validation(self):
        try:
            schema_validation=True
            data=pd.read_csv(self.config.unzip_data)              # read dataset
            all_columns=list(data.columns)                        # get dataset column names
            all_schema=self.config.all_schema.keys()              # schema column names

            # loop through dataset columns and check against schema
            for col in all_columns:
                if col == "Fraud_Label":
                    continue
                if col not in all_schema:
                    schema_validation=False
                
                with open(self.config.STATUS_FILE,"w")as file:
                    file.write(f"schema validation:{schema_validation}")
        
        except Exception as e:
            raise e
        
        return schema_validation
                    

    