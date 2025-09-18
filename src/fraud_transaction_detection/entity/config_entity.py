from pathlib import Path
from dataclasses import dataclass 


"""DataIngestionConfig class will return directories for download data,zip data,extract data path and 
source url for data ingestion process """
@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path 
    source_url: str
    local_data_file: Path
    unzip_dir: Path


"""DataValidationConfig class will return
dataset path,data validation folder,target column, all_columns from schema 
for data validation process """
@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path 
    unzip_data: Path
    STATUS_FILE: Path
    all_schema: dict



"""DataTransformationConfig class will return
data transformation folder path,dataset path,target column for data transformation"""
@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    data_path: Path 
    target_col: str



"""ModelTrainerConfig class will return
model trainer folder path,traindata path,target column,model path,parameters for model trainer"""
@dataclass(frozen=True)
class ModelTrainerConfig:
    root_dir: Path
    train_data: Path
    model_name: str 
    kernel: str 
    degree: 3
    target_col:str
