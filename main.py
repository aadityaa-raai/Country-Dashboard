import sys,os

import pandas as pd

from src.Utils.exception import CustomException
from src.Utils.logger import logging

from src.Processing.Dataset_Processors.current_account_balance_processor import CurrentAccountBalanceProcessor
from src.Processing.Dataset_Processors.death_rate_processor import DeathRateProcessor
from src.Processing.Dataset_Processors.electricity_access_processor import ElectricityAccessProcessor
from src.Processing.Dataset_Processors.exports_processor import ExportsProcessor
from src.Processing.Dataset_Processors.fdi_processor import FDIProcessor
from src.Ingestion.data_ingestion import DataIngestion
from src.Entity.artifacts import DataIngestionArtifact
from src.Entity.config import TrainingPipelineConfig,DataIngestionConfig,DataProcessingConfig

if __name__=="__main__":
    try:
        training_pipeline_config=TrainingPipelineConfig()
        data_ingestion_config=DataIngestionConfig(training_pipeline_config=training_pipeline_config)
        data_ingestion=DataIngestion(data_ingestion_config=data_ingestion_config)

        logging.info("Data Ingestion Started")
        data_ingestion_artifact=data_ingestion.initiate_data_ingestion()
        logging.info("Data Ingestion Completed")


        data_preprocessing_config=DataProcessingConfig(training_pipeline_config=training_pipeline_config)

        processor_1=CurrentAccountBalanceProcessor(data_ingestion_artifact=data_ingestion_artifact,
                                                   data_processing_config=data_preprocessing_config)
        processor_2=DeathRateProcessor(data_ingestion_artifact=data_ingestion_artifact,
                                           data_processing_config=data_preprocessing_config)
        processor_3=ElectricityAccessProcessor(data_ingestion_artifact=data_ingestion_artifact,
                                           data_processing_config=data_preprocessing_config)
        processor_4=ExportsProcessor(data_ingestion_artifact=data_ingestion_artifact,
                                           data_processing_config=data_preprocessing_config)
        processor_5=FDIProcessor(data_ingestion_artifact=data_ingestion_artifact,
                                           data_processing_config=data_preprocessing_config)
        
        logging.info("Processor 1 started")
        df=processor_1.process()
        logging.info("Processor 2 started")
        df=processor_2.process()
        logging.info("Processor 3 started")
        df=processor_3.process()
        logging.info("Processor 4 started")
        df=processor_4.process()
        logging.info("Processor 5 started")
        df=processor_5.process()
        logging.info("All Processors ended")
        # logging.info("Agriculture preprocessing started")
        # df=agriculture_processor.initiate_agriculture_processing()
        # logging.info("Agriculture Processing ended")
        
        # df=preprocess_dataframe(df,processed_meta_data_dir)




    except Exception as e:
        raise CustomException(e,sys)