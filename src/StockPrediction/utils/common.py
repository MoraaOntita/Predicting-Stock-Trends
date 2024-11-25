import os
import logging

def create_directories(paths):
    """
    Creates directories for the given paths if they do not already exist.

    Args:
        paths (list): A list of directory paths to create.
    """
    logger = logging.getLogger("StockPredictionLogger")  # Reuse the project logger

    for path in paths:
        try:
            os.makedirs(path, exist_ok=True)  # Create directory if it doesn't exist
            logger.info(f"Directory created or already exists: {path}")
        except Exception as e:
            # Log any errors that occur when creating directories
            logger.error(f"Error creating directory {path}: {e}")
