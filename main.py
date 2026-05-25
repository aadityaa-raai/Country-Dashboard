import sys,os,json

import pandas as pd

from src.Utils.exception import CustomException
from src.Utils.logger import logging

from src.Processing.dataset_registry import DATASET_REGISTRY
from src.Processing.dataset_processor import DatasetProcessor
from src.Ingestion.data_ingestion import DataIngestion
from src.Entity.artifacts import DataIngestionArtifact,DataProcessingArtifact,SectionProcessingArtifact
from src.Entity.config import TrainingPipelineConfig,DataIngestionConfig,DataProcessingConfig,SectionProcessingConfig
from src.Section_Processing.section_processor import process_section

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

        section_processing_config=SectionProcessingConfig(training_pipeline_config=training_pipeline_config)
        
        logging.info(
            "Economy Section Processing Started"
        )

        SECTIONS = [ "economy", "demographics", "trade", "technology", "environment", "industry", "military" ]

        for section in SECTIONS: 
            logging.info( f"{section} section processing started" )
            process_section(section_name=section, 
                            data_processing_artifact=( data_processing_artifact ),
                             section_processing_config=( section_processing_config ) )
            logging.info( f"{section} section processing completed" )

        logging.info(
            "Economy Section Processing Completed"
        )

        section_processing_artifact:SectionProcessingArtifact=section_processing_config.artifact()

        data_registry=section_processing_artifact.section_registry

        file_path=os.path.join(training_pipeline_config.artifact_dir,"data")

        os.makedirs(file_path,exist_ok=True)

        json_file=os.path.join(file_path,"data_registry.json")

        with open(json_file, "w") as file:

                json.dump(
                    data_registry,
                    file,
                    indent=4
                )


        # print(section_processing_artifact.section_registry)



    except Exception as e:
        raise CustomException(e,sys)