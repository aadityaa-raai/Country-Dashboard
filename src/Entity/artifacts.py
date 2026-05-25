from dataclasses import dataclass


@dataclass
class DataIngestionArtifact:
    raw_data_dir: str
    # processed_data_dir: str
    cache_data_dir: str
    # final_dataset_path: str
    metadata_file_path: str

@dataclass
class DataProcessingArtifact:

    processed_data_dir: str

    meta_data_dir:str

    processed_data_info: str

@dataclass
class SectionProcessingArtifact:

    section_data_dir: str

