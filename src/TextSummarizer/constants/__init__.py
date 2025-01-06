from pathlib import Path

CONFIG_FILE_PATH = Path("config/config.yaml")  
PARAMS_FILE_PATH = Path("params.yaml")


'''from pathlib import Path

# Define file paths as Path objects
CONFIG_FILE_PATH = Path("config/config.yaml")  # Use forward slashes to avoid escape sequence issues
PARAMS_FILE_PATH = Path("params.yaml")

# Assuming DataIngestionConfig is defined or imported
class DataIngestionConfig:
    def __init__(self, root_dir, source_URL, local_data_file, unzip_dir):
        self.root_dir = root_dir
        self.source_URL = source_URL
        self.local_data_file = local_data_file
        self.unzip_dir = unzip_dir

# ConfigurationManager class
class ConfigurationManager:
    def __init__(self, config_filepath=CONFIG_FILE_PATH, params_filepath=PARAMS_FILE_PATH):
        # Make sure you're passing string paths if required by read_yaml
        self.config = read_yaml(str(config_filepath))  # Convert Path object to string
        self.params = read_yaml(str(params_filepath))  # Convert Path object to string

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        # Extract data ingestion config from the loaded YAML config
        config = self.config['data_ingestion']  # Assuming 'data_ingestion' is a key in your config YAML
        
        # Create directories if needed
        create_directories([config['root_dir']])
        
        # Create and return DataIngestionConfig object
        data_ingestion_config = DataIngestionConfig(
            root_dir=config['root_dir'],
            source_URL=config['source_URL'],
            local_data_file=config['local_data_file'],
            unzip_dir=config['unzip_dir']
        )
        
        return data_ingestion_config

'''