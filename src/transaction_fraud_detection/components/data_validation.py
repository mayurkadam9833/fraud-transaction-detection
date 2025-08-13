import pandas as pd 
from src.transaction_fraud_detection.entity.config_entity import DataValidationConfig


class DataValidation:
    def __init__(self,config:DataValidationConfig):
        self.config=config

    def validation(self):
        try:
            validation_status=None

            data=pd.read_csv(self.config.unzip_data_path)
            all_columns=list(data.columns)
            all_schema=self.config.schema.keys()

            for col in all_columns:
                if col not in all_schema:
                    validation_status=False
                    print(col)
                    with open(self.config.STATUS_FILE,"w")as file:
                        file.write(f"Validation status: {validation_status}")
                
                else:
                    validation_status=True
                    with open(self.config.STATUS_FILE,"w")as file:
                        file.write(f"Validation status: {validation_status}")
        
        except Exception as e:
            raise e