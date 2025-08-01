import os 
import logging 
from pathlib import Path 

# logging setup 
logging.basicConfig(level=logging.INFO,format="[%(asctime)s : %(message)s:]")

project_name="transaction_fraud_detection"

list_of_files=[ 
    f"src/{project_name}/__init__.py", 
    f"src/{project_name}/components/__init__.py", 
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/utils/__init__.py", 
    f"src/{project_name}/utils/common.py", 
    f"src/{project_name}/config/__init__.py", 
    f"src/{project_name}/config/configuration.py", 
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml", 
    "schema.yaml", 
    "main.py", 
    "app.py",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"
]

# creating project directories and files 
for filepath in list_of_files: 
    filepath=Path(filepath)
    # splitting file directory and file 
    file_dir,file_name=os.path.split(filepath)

    if file_dir != "":
        os.makedirs(file_dir,exist_ok=True) 
        logging.info(f"creating {file_dir} for {file_name}")
    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0): 
        with open(filepath,"w") as f: 
            pass 
        logging.info(f"creating empty {file_name}")
    
    else: 
        logging.info(f"{file_name} already exists")

