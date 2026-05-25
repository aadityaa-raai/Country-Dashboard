import sys

from src.Utils.exception import (
    CustomException
)

from src.Entity.config import SectionProcessingConfig
from src.Entity.artifacts import DataProcessingArtifact

from src.Section_Processing.section_utils import (
    load_section_datasets,
    merge_datasets,
    save_section_dataset
)

def process_section(

        section_name:str,

        data_processing_artifact:DataProcessingArtifact,

        section_processing_config:SectionProcessingConfig
):

    try:

        dataframes = load_section_datasets(

            section_name=section_name,

            data_processing_artifact=(
                data_processing_artifact
            )
        )

        final_df = merge_datasets(
            dataframes
        )

        save_section_dataset(

            final_df=final_df,

            section_name=section_name,

            section_processing_config=(
                section_processing_config
            )
        )

        return final_df

    except Exception as e:
        raise CustomException(e, sys)
