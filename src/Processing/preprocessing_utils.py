import pandas as pd
import numpy as np
import sys,os,json
import pycountry

from src.Utils.logger import logging
from src.Utils.exception import CustomException


REQUIRED_COLUMNS = [
    "Country",
    "Country_Code",
    "Year",
    "Value",
    "Indicator"
]


def load_data(file_path: str) -> pd.DataFrame:

    try:

        logging.info(f"Loading data from {file_path}")

        dataframe = pd.read_csv(file_path)

        logging.info("Data loaded successfully")

        return dataframe

    except Exception as e:
        raise CustomException(e, sys)


def validate_schema(dataframe: pd.DataFrame):

    try:

        missing_columns = [

            column

            for column in REQUIRED_COLUMNS

            if column not in dataframe.columns
        ]

        if missing_columns:

            raise ValueError(
                f"Missing columns: {missing_columns}"
            )

        logging.info("Schema validation successful")

    except Exception as e:
        raise CustomException(e, sys)


def standardize_columns(
        dataframe: pd.DataFrame
) -> pd.DataFrame:

    try:

        logging.info("Standardizing columns")

        dataframe.columns = [

            column.strip()

            for column in dataframe.columns
        ]

        dataframe["Country"] = (
            dataframe["Country"]
            .astype(str)
            .str.strip()
        )

        dataframe["Country_Code"] = (
            dataframe["Country_Code"]
            .astype(str)
            .str.strip()
            .str.upper()
        )

        dataframe["Indicator"] = (
            dataframe["Indicator"]
            .astype(str)
            .str.strip()
            .str.lower()
        )

        logging.info("Column standardization completed")

        return dataframe

    except Exception as e:
        raise CustomException(e, sys)


def convert_dtypes(
        dataframe: pd.DataFrame
) -> pd.DataFrame:

    try:

        logging.info("Converting datatypes")

        dataframe["Year"] = pd.to_numeric(
            dataframe["Year"],
            errors="coerce"
        )

        dataframe["Value"] = pd.to_numeric(
            dataframe["Value"],
            errors="coerce"
        )

        dataframe["Year"] = (
            dataframe["Year"]
            .astype("Int64")
        )

        logging.info("Datatype conversion completed")

        return dataframe

    except Exception as e:
        raise CustomException(e, sys)


def handle_missing_values(
        dataframe: pd.DataFrame
) -> pd.DataFrame:

    try:

        logging.info("Handling missing values")

        initial_shape = dataframe.shape

        dataframe = dataframe.dropna(

            subset=[
                "Country",
                "Country_Code",
                "Year"
            ]
        )

        dataframe = dataframe.dropna(
            subset=["Value"]
        )

        logging.info(
            f"Missing value handling completed "
            f"from {initial_shape} to "
            f"{dataframe.shape}"
        )

        return dataframe

    except Exception as e:
        raise CustomException(e, sys)


def remove_duplicates(
        dataframe: pd.DataFrame
) -> pd.DataFrame:

    try:

        logging.info("Removing duplicates")

        initial_shape = dataframe.shape

        dataframe = dataframe.drop_duplicates(

            subset=[
                "Country",
                "Country_Code",
                "Year",
                "Indicator"
            ]
        )

        logging.info(
            f"Duplicates removed "
            f"from {initial_shape} "
            f"to {dataframe.shape}"
        )

        return dataframe

    except Exception as e:
        raise CustomException(e, sys)


def filter_valid_years(
        dataframe: pd.DataFrame,
        min_year: int = 1960,
        max_year: int = 2035
) -> pd.DataFrame:

    try:

        logging.info("Filtering valid years")

        dataframe = dataframe[

            (dataframe["Year"] >= min_year) &
            (dataframe["Year"] <= max_year)

        ]

        logging.info("Year filtering completed")

        return dataframe

    except Exception as e:
        raise CustomException(e, sys)


def sort_dataframe(
        dataframe: pd.DataFrame
) -> pd.DataFrame:

    try:

        logging.info("Sorting dataframe")

        dataframe = dataframe.sort_values(

            by=[
                "Country",
                "Year"
            ]

        ).reset_index(drop=True)

        logging.info("Sorting completed")

        return dataframe

    except Exception as e:
        raise CustomException(e, sys)


def get_year_range(
        dataframe: pd.DataFrame
) -> dict:

    try:

        min_year = int(
            dataframe["Year"].min()
        )

        max_year = int(
            dataframe["Year"].max()
        )

        return {

            "min_year": min_year,

            "max_year": max_year
        }

    except Exception as e:
        raise CustomException(e, sys)


def find_missing_years(
        dataframe: pd.DataFrame
) -> list:

    try:

        available_years = set(
            dataframe["Year"].dropna().unique()
        )

        full_range = set(

            range(
                int(dataframe["Year"].min()),
                int(dataframe["Year"].max()) + 1
            )
        )

        missing_years = sorted(
            list(full_range - available_years)
        )

        return missing_years

    except Exception as e:
        raise CustomException(e, sys)


def get_dataset_metadata(
        dataframe: pd.DataFrame
) -> dict:

    try:

        year_range = get_year_range(dataframe)

        metadata = {

            "total_rows": len(dataframe),

            "total_countries": (
                dataframe["Country"]
                .nunique()
            ),

            "min_year": year_range["min_year"],

            "max_year": year_range["max_year"],

            "missing_years": (
                find_missing_years(dataframe)
            )
        }

        return metadata

    except Exception as e:
        raise CustomException(e, sys)

def save_metadata(
        metadata: dict,
        file_path: str
):

    try:

        os.makedirs(
            os.path.dirname(file_path),
            exist_ok=True
        )

        with open(file_path, "w") as file:

            json.dump(
                metadata,
                file,
                indent=4
            )

        logging.info(
            f"Metadata saved at {file_path}"
        )

    except Exception as e:
        raise CustomException(e, sys)

def save_processed_dataframe(
        dataframe:pd.DataFrame,
        file_path:str
):

    try:

        os.makedirs(

            os.path.dirname(file_path),

            exist_ok=True
        )

        dataframe.to_csv(

            file_path,

            index=False
        )

        logging.info(
            f"Processed dataframe saved at "
            f"{file_path}"
        )

    except Exception as e:
        raise CustomException(e, sys)

def preprocess_dataframe(
        dataframe: pd.DataFrame
):

    try:

        logging.info(
            "Starting preprocessing pipeline"
        )

        validate_schema(dataframe)

        dataframe = standardize_columns(
            dataframe
        )

        dataframe = convert_dtypes(
            dataframe
        )

        dataframe = handle_missing_values(
            dataframe
        )

        dataframe = remove_duplicates(
            dataframe
        )

        dataframe = filter_valid_years(
            dataframe
        )

        dataframe = sort_dataframe(
            dataframe
        )

        metadata = get_dataset_metadata(
            dataframe
        )

        # save_metadata(metadata=metadata,file_path=file_path)

        logging.info(
            "Preprocessing pipeline completed"
        )

        return dataframe,metadata

    except Exception as e:
        raise CustomException(e, sys)


def process_dataset(
        raw_file_path,
        processed_file_path,
        metadata_file_path,
        value_column_name
):

    try:

        dataframe = load_data(
            raw_file_path
        )

        dataframe, metadata = (
            preprocess_dataframe(
                dataframe
            )
        )

        dataframe.rename(

            columns={
                "Value": value_column_name
            },

            inplace=True
        )

        save_processed_dataframe(

            dataframe,

            processed_file_path
        )

        save_metadata(

            metadata,

            metadata_file_path
        )

        logging.info(
            f"{value_column_name} "
            f"processing completed"
        )

        return dataframe

    except Exception as e:
        raise CustomException(e, sys)