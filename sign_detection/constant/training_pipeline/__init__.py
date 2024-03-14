import os

ARTIFACTS_DIR:str="artifacts"

DATA_INGESTION_DIR_NAME:str="data_ingestion"

LOCAL_DATA_FILE="data.zip"

DATA_INGESTION_FEATURE_STORE_DIR:str="feature_store"

DATA_DOWNLOAD_URL:str="https://drive.google.com/file/d/1lijGILl9xcaXkkYiIka45zh8kukeiwp1/view?usp=sharing"



DATA_VALIDATION_DIR_NAME: str = "data_validation"

DATA_VALIDATION_STATUS_FILE = 'status.txt'

DATA_VALIDATION_ALL_REQUIRED_FILES = ["train", "test","valid","data.yaml"]


MODEL_TRAINER_DIR_NAME:str="model_trainer"

MODEL_TRAINER_PRETRAINED_WEIGHT_NAME:str="yolov5s.pt"

MODEL_TRAINER_NO_EPOCHS:int= 2

MODEL_TRAINER_BATCH_SIZE:int=4