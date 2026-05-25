import os
import sys

from src.Utils.logger import logging
from src.Utils.exception import CustomException

from src.Entity.config import (
    DataProcessingConfig
)

from src.Entity.artifacts import (
    DataIngestionArtifact
)

from src.Processing.preprocessing_utils import (
    load_data,
    preprocess_dataframe,
    save_metadata
)


class ForexReservesProcessor:

    def __init__(
            self,
            data_ingestion_artifact: DataIngestionArtifact,
            data_processing_config: DataProcessingConfig
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


    def initiate_forex_reserves_processing(self):

        try:

            logging.info(
                "Forex reserves processing started"
            )

            raw_file_path = os.path.join(

                self.data_ingestion_artifact.raw_data_dir,

                "forex_reserves_raw.csv"
            )

            dataframe = load_data(
                raw_file_path
            )

            dataframe, metadata = (
                preprocess_dataframe(
                    dataframe
                )
            )

            dataframe = dataframe.rename(

                columns={
                    "Value": "Forex_Reserves"
                }
            )

            os.makedirs(

                self.data_processing_config.processed_data_dir,

                exist_ok=True
            )

            processed_file_path = os.path.join(

                self.data_processing_config.processed_data_dir,

                "forex_reserves_data.csv"
            )

            dataframe.to_csv(

                processed_file_path,

                index=False
            )

            logging.info(
                "Forex reserves processed csv saved"
            )

            metadata_file_path = os.path.join(

                self.data_processing_config.meta_data_dir,

                "forex_reserves_metadata.json"
            )

            save_metadata(

                metadata=metadata,

                file_path=metadata_file_path
            )

            logging.info(
                "Forex reserves metadata saved"
            )

            logging.info(
                "Forex reserves processing completed"
            )

            return dataframe

        except Exception as e:
            raise CustomException(e, sys)