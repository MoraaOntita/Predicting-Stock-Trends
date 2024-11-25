import yaml
import os
from src.StockPrediction import logger

class ConfigurationManager:
    def __init__(self, config_path="config/config.yaml"):
        self.config_path = config_path
        self.config = self.read_config()

    def read_config(self):
        try:
            # Log the loading of the configuration file
            logger.info(f"Reading configuration from {self.config_path}")
            
            with open(self.config_path, "r") as file:
                config_data = yaml.safe_load(file)

            # Log successful loading of the config
            logger.info(f"Configuration file loaded successfully")
            return config_data
        except Exception as e:
            # Log any error encountered while reading the config
            logger.error(f"Failed to read configuration file: {e}")
            raise e

    def get_data_ingestion_config(self):
        try:
            # Retrieve 'data_ingestion' config and log the action
            data_ingestion_config = self.config.get("data_ingestion", {})
            root_dir = data_ingestion_config.get("root_dir", "")
            
            # Log the root directory being used
            logger.info(f"Using root directory: {root_dir}")

            # Join the root directory with the relative path of raw data
            raw_data_path = os.path.join(root_dir, data_ingestion_config.get("raw_data_path", ""))
            
            # Updating raw_data_path to be an absolute path
            data_ingestion_config["raw_data_path"] = raw_data_path

            # Log the final data path used for saving
            logger.info(f"Final data ingestion path: {raw_data_path}")
            
            return data_ingestion_config

        except Exception as e:
            # Log any error encountered while accessing the 'data_ingestion' config
            logger.error(f"Error retrieving data ingestion configuration: {e}")
            raise e
