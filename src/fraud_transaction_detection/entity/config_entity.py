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
    all_columns: dict
