import os
from dataclasses import dataclass
from datetime import datetime
from sign_detection.constant.training_pipeline import *




TIMESTAMP:str=datetime.now().strftime('%m_%d_%y_%H_%M_%S')


@dataclass
class TrainingPipelineConfig:
    artifacts_dir:str=os.path.join(ARTIFACTS_DIR,TIMESTAMP)

trainig_pipeline_config:TrainingPipelineConfig=TrainingPipelineConfig()

@dataclass
class DataIngestionConfig:
    data_ingestion_dir=os.path.join(trainig_pipeline_config.artifacts_dir,DATA_INGESTION_DIR_NAME)

    feature_store_file_path:str=os.path.join(data_ingestion_dir,DATA_INGESTION_FEATURE_STORE_DIR)

    local_data_file_path:str=os.path.join(data_ingestion_dir,LOCAL_DATA_FILE)

    data_download_url:str=DATA_DOWNLOAD_URL