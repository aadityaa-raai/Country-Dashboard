import os
import sys
import json
import requests
import pandas as pd

from src.Entity.config import DataIngestionConfig
from src.Entity.artifacts import DataIngestionArtifact

from src.Ingestion.sources import WORLD_BANK_INDICATORS

from src.Utils.exception import CustomException
from src.Utils.logger import logging

class DataIngestion:

    def __init__(self,
                 data_ingestion_config: DataIngestionConfig
                 ):
        try:

            self.data_ingestion_config = data_ingestion_config

        except Exception as e:
            raise CustomException(e, sys)


    def fetch_indicator_data(self,
                             indicator_name,
                             indicator_code
                             ):
        try:

            url = (
                f"https://api.worldbank.org/v2/"
                f"country/IND/indicator/"
                f"{indicator_code}"
                f"?format=json&per_page=20000"
            )

            logging.info(f"Fetching {indicator_name}")

            response = requests.get(url)

            response.raise_for_status()

            return response.json()

        except Exception as e:
            raise CustomException(e, sys)


    def json_to_dataframe(self,
                          data,
                          indicator_name
                          ):
        try:

            records = []

            for item in data[1]:

                records.append({

                    "Country": item["country"]["value"],

                    "Country_Code": item["countryiso3code"],

                    "Year": item["date"],

                    "Value": item["value"],

                    "Indicator": indicator_name

                })

            dataframe = pd.DataFrame(records)

            return dataframe

        except Exception as e:
            raise CustomException(e, sys)


    def save_raw_dataset(self,
                         dataframe,
                         file_name
                         ):
        try:

            raw_data_dir = (
                self.data_ingestion_config.raw_data_dir
            )

            os.makedirs(
                raw_data_dir,
                exist_ok=True
            )

            file_path = os.path.join(
                raw_data_dir,
                file_name
            )

            dataframe.to_csv(
                file_path,
                index=False
            )

            logging.info(f"Saved {file_name}")

        except Exception as e:
            raise CustomException(e, sys)


    def save_metadata(self,metadata):

        try:

            metadata_path = (
                self.data_ingestion_config.metadata_file_path
            )

            os.makedirs(
                os.path.dirname(metadata_path),
                exist_ok=True
            )

            with open(metadata_path, "w") as file:

                json.dump(
                    metadata,
                    file,
                    indent=4
                )

        except Exception as e:
            raise CustomException(e, sys)


    def initiate_data_ingestion(self):

        try:

            metadata = {}

            for indicator_name, indicator_code in WORLD_BANK_INDICATORS.items():

                data = self.fetch_indicator_data(
                    indicator_name,
                    indicator_code
                )

                dataframe = self.json_to_dataframe(
                    data,
                    indicator_name
                )

                file_name = f"{indicator_name}_raw.csv"

                self.save_raw_dataset(
                    dataframe,
                    file_name
                )

                metadata[indicator_name] = {

                    "indicator_code": indicator_code,

                    "raw_file": file_name

                }

            self.save_metadata(metadata)

            data_ingestion_artifact = (
                DataIngestionArtifact(

                    raw_data_dir=(
                        self.data_ingestion_config.raw_data_dir
                    ),

                    cache_data_dir=(
                        self.data_ingestion_config.cache_data_dir
                    ),

                    metadata_file_path=(
                        self.data_ingestion_config.metadata_file_path
                    )
                )
            )

            return data_ingestion_artifact

        except Exception as e:
            raise CustomException(e, sys)