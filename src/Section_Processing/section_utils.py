import os
import sys
import json
import pandas as pd

from src.Entity.config import SectionProcessingConfig
from src.Entity.artifacts import DataProcessingArtifact

from src.Utils.exception import (
    CustomException
)

from src.Utils.logger import logging


def load_section_datasets(
        section_name:str,
        data_processing_artifact:DataProcessingArtifact
):

    try:

        section_info_dir = os.path.join(

            data_processing_artifact
            .processed_data_info,

            section_name
        )

        dataset_info_files = os.listdir(
            section_info_dir
        )

        dataframes = []

        for dataset_info_file in dataset_info_files:

            dataset_info_path = os.path.join(

                section_info_dir,

                dataset_info_file
            )

            with open(
                dataset_info_path,
                "r"
            ) as file:

                dataset_info = json.load(file)

            dataset_path = dataset_info[
                "data_path"
            ]

            df = pd.read_csv(
                dataset_path
            )

            df.drop(columns=['Indicator'],inplace=True)

            dataframes.append(df)
        
        logging.info(f"{section_name} csv files fetched to dataframes.")

        # print(dataframes)


        return dataframes

    except Exception as e:
        raise CustomException(e, sys)


def merge_datasets(
        dataframes:list[pd.DataFrame]
):

    try:

        final_df = dataframes[0]

        for df in dataframes[1:]:

            final_df = final_df.merge(

                df,

                on=[
                    "Country",
                    "Country_Code",
                    "Year"
                ],

                how="outer"
            )

        return final_df

    except Exception as e:
        raise CustomException(e, sys)


def save_section_dataset(

        final_df:pd.DataFrame,

        section_name:str,

        section_processing_config:SectionProcessingConfig
):

    try:

        os.makedirs(

            section_processing_config
            .section_data_dir,

            exist_ok=True
        )

        output_file_path = os.path.join(

            section_processing_config
            .section_data_dir,

            f"{section_name}_data.csv"
        )

        final_df.to_csv(

            output_file_path,

            index=False
        )

        return output_file_path

    except Exception as e:
        raise CustomException(e, sys)
