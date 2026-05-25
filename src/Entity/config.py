import os
from datetime import datetime


class TrainingPipelineConfig:
    def __init__(self, timestamp=datetime.now()):

        timestamp = timestamp.strftime("%m_%d_%Y_%H_%M_%S")

        self.pipeline_name = "country_dashboard"
        self.artifact_dir = os.path.join("artifacts", timestamp)
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
