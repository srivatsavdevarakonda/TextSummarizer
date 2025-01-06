from TextSummarizer.constants import *
from TextSummarizer.utils.common import read_yaml, create_directories

from TextSummarizer.entity import (DataIngestionConfig)


class ConfigurationManager:
    def __init__(self, config_filepath = CONFIG_FILE_PATH, params_filepath = PARAMS_FILE_PATH):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        create_directories([self.config.artifacts_root]) 


    def get_data_ingestion_config(self) -> DataIngestionConfig:
        
        # Extracting the data ingestion configuration from the self.config object
        config = self.config.data_ingestion
        
        # Creating necessary directories for the root directory
        create_directories([config.root_dir])
        
        # Creating the DataIngestionConfig object
        data_ingestion_config = DataIngestionConfig(root_dir=config.root_dir, source_URL=config.source_URL, local_data_file=config.local_data_file, unzip_dir=config.unzip_dir)
        
        # Returning the data ingestion configuration object
        return data_ingestion_config
            