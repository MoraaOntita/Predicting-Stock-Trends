import logging
from src.StockPrediction.components.data_ingestion import DataIngestion
from src.StockPrediction.config.configuration import ConfigurationManager
from src.StockPrediction.entity.config_entity import DataIngestionConfig

class TrainingPipeline:
    def __init__(self):
        self.config_manager = ConfigurationManager()
        self.logger = logging.getLogger("StockPredictionLogger")  # Reuse your logger

    def start(self):
        try:
            # Log the start of the data ingestion process
            self.logger.info("Starting data ingestion process...")

            # Load data ingestion config
            ingestion_config = DataIngestionConfig(**self.config_manager.get_data_ingestion_config())

            # Perform data ingestion
            data_ingestion = DataIngestion(config=ingestion_config)
            data_ingestion.download_data()

            # Log the successful completion of data ingestion
            self.logger.info("Data ingestion completed successfully.")

        except Exception as e:
            # Log any errors during the pipeline execution
            self.logger.error(f"Error occurred in the data ingestion pipeline: {e}")
            raise  # Re-raise the exception to allow higher-level handling (optional)
