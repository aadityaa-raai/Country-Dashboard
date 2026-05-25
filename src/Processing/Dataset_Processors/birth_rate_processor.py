import os
import sys

from src.Utils.exception import CustomException

from src.Entity.config import (
    DataProcessingConfig
)

from src.Entity.artifacts import (
    DataIngestionArtifact
)

from src.Processing.preprocessing_utils import (
    process_dataset
)


class BirthRateProcessor:

    def __init__(
            self,
            data_ingestion_artifact,
            data_processing_config
    ):

        try:

            self.data_ingestion_artifact = (
                data_ingestion_artifact
            )

            self.data_processing_config = (
                data_processing_config
            )

        except Exception as e:
            raise CustomException(e, sys)


    def process(self):

        try:

            raw_file_path = os.path.join(

                self.data_ingestion_artifact.raw_data_dir,

                "birth_rate_raw.csv"
            )

            processed_file_path = os.path.join(

                self.data_processing_config.processed_data_dir,

                "birth_rate_data.csv"
            )

            metadata_file_path = os.path.join(

                self.data_processing_config.meta_data_dir,

                "birth_rate_metadata.json"
            )

            return process_dataset(

                raw_file_path=raw_file_path,

                processed_file_path=processed_file_path,

                metadata_file_path=metadata_file_path,

                value_column_name="Birth_Rate"
            )

        except Exception as e:
            raise CustomException(e, sys)