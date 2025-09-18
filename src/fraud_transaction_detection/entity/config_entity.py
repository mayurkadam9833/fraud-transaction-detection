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
