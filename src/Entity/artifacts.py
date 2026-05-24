from dataclasses import dataclass


@dataclass
class DataIngestionArtifact:
    raw_data_dir: str
    processed_data_dir: str
    cache_data_dir: str
    final_dataset_path: str
    metadata_file_path: str


@dataclass
class DataProcessingArtifact:
    processed_file_path: str
    country_summary_file_path: str


@dataclass
class ForecastArtifact:
    forecast_file_path: str
    model_name: str


@dataclass
class VisualizationArtifact:
    chart_export_dir: str
    dashboard_snapshot_dir: str

