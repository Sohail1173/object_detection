import os
import sys
# from six.moves import urllib
import zipfile
from sign_detection.logger import logging
from sign_detection.exception import signException
from sign_detection.entity.config_entity import DataIngestionConfig
from sign_detection.entity.artifacts_entity import DataIngestionArtifact
import gdown

class DataIngestion:
    def __init__(self,data_ingestion_config:DataIngestionConfig=DataIngestionConfig()):
        try:
            self.data_ingestion_config=data_ingestion_config
        except Exception as e:
            raise signException(e,sys) 
    
    def download_data(self) ->str:
        """
        fetch data from the url
        
        """

        try:
            dataset_url=self.data_ingestion_config.data_download_url
            zip_download_dir=self.data_ingestion_config.data_ingestion_dir
            zip_download=self.data_ingestion_config.local_data_file_path
            os.makedirs(zip_download_dir,exist_ok=True)
            logging.info(f"Downloading data  from {dataset_url} to {zip_download_dir}")
            file_id=dataset_url.split('/')[-2]
            prefix = 'https://drive.google.com/uc?/export=download&id='
            gdown.download(prefix+file_id,zip_download)
            logging.info(f"downloaded data from {dataset_url} to {zip_download_dir}")
            # return zip_download_dir
            return zip_download
        except Exception as e:
            raise signException(e,sys)
        
    def extract_zip_file(self,zip_file_path:str) ->str:
        """"
        zip_file-path:str
        Extract the zip file into the given directory

        function returns None
        
        """
        try:
            feature_store_path=self.data_ingestion_config.feature_store_file_path
            os.makedirs(feature_store_path,exist_ok=True)
            with zipfile.ZipFile(zip_file_path,"r") as zip_ref:
                zip_ref.extractall(feature_store_path)
            logging.info(f"Extracted data from {zip_file_path} to {feature_store_path}")
            return feature_store_path
        except Exception as e:
            raise signException(e,sys)
        

    def initiate_data_ingestion(self)-> DataIngestionArtifact:
        logging.info("Entered initiate_data_ingestion method of data_ingestion class")

        try:
            zip_file_path=self.download_data()
            feature_store_path=self.extract_zip_file(zip_file_path)

            data_ingestion_artifact=DataIngestionArtifact(
                data_zip_file_path=zip_file_path,
                feature_store_path =feature_store_path)
            
            logging.info("Exited initiate_data_ingestion method of data_ingestion class")
            logging.info(f"Data Ingestion artifact:{data_ingestion_artifact}")
            return data_ingestion_artifact
        except Exception as e:
            raise signException(e,sys)