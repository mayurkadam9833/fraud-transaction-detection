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
def read_yaml(path_to_yaml: Path) ->ConfigBox: 
    try:
        with open(path_to_yaml) as yaml_file:
            content=yaml.safe_load(yaml_file)
            logger.info(f"yaml_file{path_to_yaml} loaded sucessfully")
            return ConfigBox(content)
    
    except BoxValueError:
        raise ValueError("yaml_file_is_empty")
    except Exception as e: 
        raise e
  
