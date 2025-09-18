from src.fraud_transaction_detection.config.configuration import ConfigManager 
from src.fraud_transaction_detection.components.data_transfromation import DataTransformation


"""
DataTransformationPipeline class is pipeline to preprocess data 
[encoding,oversampling,scaling,split into tarin & test]
"""
class DataTransformationPipeline:
    def __init__(self):
        pass

    def main(self):              
        config=ConfigManager()                                                       # create object of configmanager      
        data_transformation_config=config.get_data_transformation_config()           # get data transformation config
        data_transformation=DataTransformation(config=data_transformation_config)    # create object of data transformation
        data_transformation.data_preprocessing()                                     # preprocess data
        data_transformation.encoding()                                               # encode categorical data
        data_transformation.oversampling_scaling_split()                             # perform oversampling scaling & split operations

