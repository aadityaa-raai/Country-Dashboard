import os
import sys
import json

from src.Processing.processed_data_registry import PROCESSED_DATA_REGISTRY

from src.Utils.exception import (
    CustomException
)

from src.Entity.config import (
    DataProcessingConfig
)

from src.Entity.artifacts import (
    DataIngestionArtifact
)

from src.Processing.dataset_registry import (
    DATASET_REGISTRY
)

from src.Processing.preprocessing_utils import (
    process_dataset
)


class DatasetProcessor:

    def __init__(
            self,
            dataset_name,
            data_ingestion_artifact:DataIngestionArtifact,
            data_processing_config:DataProcessingConfig
    ):

        try:

            self.dataset_name = dataset_name

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

            self.dataset_config = (
                DATASET_REGISTRY[
                    self.dataset_name
                ]
            )

            raw_file_path = os.path.join(

                self.data_ingestion_artifact.raw_data_dir,

                f"{self.dataset_name}_raw.csv"
            )

            processed_file_path = os.path.join(

                self.data_processing_config.processed_data_dir,

                f"{self.dataset_name}_data.csv"
            )

            metadata_file_path = os.path.join(

                self.data_processing_config
                .meta_data_dir,

                f"{self.dataset_name}_metadata.json"
            )

            section_file_path=os.path.join(self.data_processing_config.processed_data_info,self.dataset_config.get("section"))
            os.makedirs(section_file_path,exist_ok=True)

            file_path=os.path.join(section_file_path,f"{self.dataset_name}_info.json")
            # os.makedirs(file_path,exist_ok=True)

            PROCESSED_DATA_REGISTRY = {
                                    "data_path": processed_file_path,
                                    "metadata_path": metadata_file_path,
                                    "value_column": self.dataset_config["value_column"],
                                    "section": self.dataset_config.get("section")
                                    }
            
            with open(file_path, "w") as file:

                json.dump(
                    PROCESSED_DATA_REGISTRY,
                    file,
                    indent=4
                )

            return process_dataset(

                raw_file_path=raw_file_path,

                processed_file_path=processed_file_path,

                metadata_file_path=metadata_file_path,

                value_column_name=(
                    self.dataset_config[
                        "value_column"
                    ]
                )
            )

        except Exception as e:
            raise CustomException(e, sys)