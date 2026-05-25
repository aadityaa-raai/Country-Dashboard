from dataclasses import dataclass


@dataclass
class DataIngestionArtifact:
    raw_data_dir: str
    # processed_data_dir: str
    cache_data_dir: str
    # final_dataset_path: str
    metadata_file_path: str


