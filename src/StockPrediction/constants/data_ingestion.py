import os

# Ticker Symbol for S&P 500
TICKER_SYMBOL = '^GSPC'

# Default Start and End Dates for Data Fetching
DEFAULT_START_DATE = '2000-01-01'
DEFAULT_END_DATE = '2023-11-01'

# Raw Data Folder and File Path
RAW_DATA_FOLDER = 'artifacts/data_ingestion'
RAW_DATA_FILENAME = 'SP500_historical_data.csv'

# Full Path to Raw Data CSV (constructed from the folder and filename)
RAW_DATA_PATH = os.path.join(RAW_DATA_FOLDER, RAW_DATA_FILENAME)