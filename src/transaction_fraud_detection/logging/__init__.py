import os 
import sys 
import logging 

log_str="[%(asctime)s : %(modulename)s : %(levelname)s : %(message)s]"

curr_dir=os.path.abspath(os.path.dirname(__file__))
log_dir=os.path.join(curr_dir,"logs")
log_path=os.path.join(log_dir,"running_logs.log")
os.makedirs(log_dir,exist_ok=True)

logging.basicConfig(
    level=logging.INFO, 
    format=log_str, 
    handlers=[ 
        logging.FileHandler(log_path),
        logging.StreamHandler(sys.stdout)
    ]
)

logger=logging.getLogger("transcation_fraud_detection")