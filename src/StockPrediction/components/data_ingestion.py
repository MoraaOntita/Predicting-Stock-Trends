import yfinance as yf
import os
from src.StockPrediction.constants.data_ingestion import TICKER_SYMBOL, DEFAULT_START_DATE, DEFAULT_END_DATE, RAW_DATA_PATH

class DataIngestion:
    def __init__(self, config):
        self.config = config

    def download_data(self):
        os.makedirs(os.path.dirname(self.config.raw_data_path), exist_ok=True)

        # Download data using constants for the ticker symbol and dates
        data = yf.download(
            TICKER_SYMBOL,
            start=self.config.start_date or DEFAULT_START_DATE,
            end=self.config.end_date or DEFAULT_END_DATE
        )

        # Save data to CSV
        data.to_csv(self.config.raw_data_path or RAW_DATA_PATH)
        print(f"Data saved to {self.config.raw_data_path or RAW_DATA_PATH}")
