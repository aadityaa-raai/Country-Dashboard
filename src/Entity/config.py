import os, json
from datetime import datetime

from src.Entity.artifacts import DataProcessingArtifact,SectionProcessingArtifact

class TrainingPipelineConfig:
    def __init__(self, timestamp=datetime.now()):

        # timestamp = timestamp.strftime("%m_%d_%Y_%H_%M_%S")

        self.pipeline_name = "country_dashboard"
        self.artifact_dir = os.path.join("artifacts")
        self.timestamp = timestamp


class DataIngestionConfig:
    def __init__(self, training_pipeline_config: TrainingPipelineConfig):

        self.data_ingestion_dir = os.path.join(
            training_pipeline_config.artifact_dir,
            "data_ingestion"
        )

        # Raw downloaded datasets
        self.raw_data_dir = os.path.join(
            self.data_ingestion_dir,
            "raw_data"
        )

        # Cleaned/standardized datasets
        # self.processed_data_dir = os.path.join(
        #     self.data_ingestion_dir,
        #     "processed_data"
        # )

        # Cached API responses
        self.cache_data_dir = os.path.join(
            self.data_ingestion_dir,
            "cache_data"
        )

        # Main combined dataset
        # self.final_dataset_path = os.path.join(
        #     self.processed_data_dir,
        #     "country_dashboard.csv"
        # )

        # Metadata / source tracking
        self.metadata_file_path = os.path.join(
            self.data_ingestion_dir,
            "metadata.json"
        )

class DataProcessingConfig:
    def __init__(self,training_pipeline_config:TrainingPipelineConfig):
        self.data_processing_dir=os.path.join(training_pipeline_config.artifact_dir,"data_processing")

        self.processed_data_dir=os.path.join(self.data_processing_dir,"processed_data")

        self.meta_data_dir=os.path.join(self.data_processing_dir,"metadata")

        self.processed_data_info=os.path.join(self.data_processing_dir,"processed data info")
    
    def artifact(self)->DataProcessingArtifact:
        data_processing_artifact=DataProcessingArtifact(processed_data_dir=self.processed_data_dir,
                                                        meta_data_dir=self.meta_data_dir,
                                                        processed_data_info=self.processed_data_info)

        return data_processing_artifact

class SectionProcessingConfig:

    def __init__(
            self,
            training_pipeline_config:TrainingPipelineConfig
    ):

        self.section_processing_dir = (
            os.path.join(

                training_pipeline_config
                .artifact_dir,

                "section_processing"
            )
        )

        os.makedirs(os.path.join(training_pipeline_config.artifact_dir,"data"),exist_ok=True)

        self.section_data_dir = (
            os.path.join(

                self.section_processing_dir,

                "section_data"
            )
        )

    SECTIONS = [ "economy", "demographics", "trade", "technology", "environment", "industry", "military" ]

    def artifact(self)->SectionProcessingArtifact:
        file_path=self.section_data_dir
        section_registry:dict={s: os.path.join(file_path,f"{s}_data.csv") for s in self.SECTIONS}
        
        # json_file="artifacts/data/data_registry.json"

        # # os.path.join(self.training_pipeline)

        # # os.makedirs(os.path.dirname(json_file),exist_ok=True)

        # with open(file_path,"w") as file:
        #     json.dump(section_registry,file,indent=4)

        section_processing_artifact= SectionProcessingArtifact(
            section_data_dir=self.section_data_dir,
            section_registry=section_registry
        )
        return section_processing_artifact
