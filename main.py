import sys

from src.Utils.exception import CustomException
from src.Utils.logger import logging

from src.Ingestion.data_ingestion import DataIngestion
from src.Entity.artifacts import DataIngestionArtifact
from src.Entity.config import DataIngestionConfig,TrainingPipelineConfig

if __name__=="__main__":
    try:
        training_pipeline_config=TrainingPipelineConfig()
        data_ingestion_config=DataIngestionConfig(training_pipeline_config=training_pipeline_config)
        data_ingestion=DataIngestion(data_ingestion_config=data_ingestion_config)

        logging.info("Data Ingestion Started")
        data_ingestion_artifact=data_ingestion.initiate_data_ingestion()
        logging.info("Data Ingestion Completed")


    except Exception as e:
        raise CustomException(e,sys)