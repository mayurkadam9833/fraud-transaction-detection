import os 
from box.exceptions import BoxValueError 
import yaml
from src.transaction_fraud_detection.logging import logger
import json 
import joblib 
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path 
from typing import Any 



@ensure_annotations 
def read_yaml(path_to_yaml: Path)->ConfigBox: 
    try:
        with open(path_to_yaml) as yaml_file:
            content=yaml.safe_load(yaml_file)
            logger.info(f"yaml_file{path_to_yaml} loaded sucessfully")
    except BoxValueError:
        raise ValueError("yaml_file_is_empty")
    except Exception as e: 
        raise e
    return ConfigBox(content)


@ensure_annotations 
def create_directories(path_to_directories=list,verbose=True): 
    for path in path_to_directories: 
        os.makedirs(path,exist_ok=True)
        if verbose: 
            logger.info(f"create directory at {path}")

@ensure_annotations
def get_size(file):
    size_in_kb=round(os.path.getsize(file)/1024)
    return f"File size : {size_in_kb} kb"

@ensure_annotations
def save_json(path:Path,data:dict):
    with open(path,"w")as f:
        json.dump(data,f,indent=4)

    logger.info(f"json file saved at: {path}")