import os
import urllib.request as request
import zipfile
from TextSummarizer.logging import logger
from TextSummarizer.utils.common import get_size
from pathlib import Path
from TextSummarizer import DataIngestionConfig


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            # If the file doesn't exist, download it
            filename, headers = request.urlretrieve(
                url=self.config.source_URL,
                filename=self.config.local_data_file
            )
            logger.info(f"Downloaded {filename} with following info: \n{headers}")
        else:
            # If the file exists, log its size
            file_size = os.path.getsize(Path(self.config.local_data_file))
            logger.info(f"File already exists of size: {file_size}")

    def extract_zip_file(self):
        """
        Extracts the zip file into the data directory.
        Function returns None.
        """
        unzip_path = self.config.unzip_dir  # Define the unzip path
        
        # Create the unzip directory if it doesn't exist
        os.makedirs(unzip_path, exist_ok=True)
        
        # Extract the zip file
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
