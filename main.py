import logging
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from src.StockPrediction.pipeline.stage_01_data_ingestion import DataIngestion
from src.StockPrediction.config.configuration import ConfigurationManager
from src.StockPrediction.entity.config_entity import DataIngestionConfig


def setup_logger():
    """
    Set up a logger for the main process
    """
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s: %(levelname)s: %(message)s")
    return logging.getLogger("StockPredictionLogger")

def run_data_ingestion(config):
    """
    Runs the data ingestion stage of the pipeline
    """
    try:
        logging.info("Starting the Data Ingestion Stage.")
        data_ingestion = DataIngestion(config=config)
        data_ingestion.download_data()  # Trigger the data ingestion process
        logging.info("Data Ingestion completed successfully.")
    except Exception as e:
        logging.error(f"Error occurred during Data Ingestion: {e}")
        raise e

def main():
    """
    Main function to run the data ingestion stage of the pipeline
    """
    try:
        # Setup logger for the main script
        logger = setup_logger()
        logger.info("Starting the Stock Prediction Data Ingestion Pipeline...")

        # Load the configuration manager to get the ingestion config
        config_manager = ConfigurationManager()
        ingestion_config = DataIngestionConfig(**config_manager.get_data_ingestion_config())

        # Run the data ingestion stage
        run_data_ingestion(config=ingestion_config)

        logger.info("Data Ingestion Pipeline executed successfully.")

    except Exception as e:
        # Log the error and exit
        logging.error(f"Pipeline execution failed: {e}")
        exit(1)  # Exit with an error status code (1)

if __name__ == "__main__":
    main()
