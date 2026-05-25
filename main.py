import sys,os

import pandas as pd

from src.Utils.exception import CustomException
from src.Utils.logger import logging

from src.Processing.dataset_registry import DATASET_REGISTRY
from src.Processing.dataset_processor import DatasetProcessor
from src.Ingestion.data_ingestion import DataIngestion
from src.Entity.artifacts import DataIngestionArtifact,DataProcessingArtifact
from src.Entity.config import TrainingPipelineConfig,DataIngestionConfig,DataProcessingConfig

if __name__=="__main__":
    try:
        training_pipeline_config=TrainingPipelineConfig()
        data_ingestion_config=DataIngestionConfig(training_pipeline_config=training_pipeline_config)
        data_ingestion=DataIngestion(data_ingestion_config=data_ingestion_config)

        logging.info("Data Ingestion Started")
        data_ingestion_artifact=data_ingestion.initiate_data_ingestion()
        logging.info("Data Ingestion Completed")


        data_processing_config=DataProcessingConfig(training_pipeline_config=training_pipeline_config)

        for dataset_name in DATASET_REGISTRY:

            processor = DatasetProcessor(

                dataset_name=dataset_name,

                data_ingestion_artifact=data_ingestion_artifact,

                data_processing_config=data_processing_config
                
            )

            processor.process()
        
        data_processing_artifact=data_processing_config.artifact()

        




    except Exception as e:
        raise CustomException(e,sys)