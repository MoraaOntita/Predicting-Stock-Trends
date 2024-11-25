from dataclasses import dataclass
from typing import Optional
from datetime import datetime

@dataclass
class DataIngestionConfig:
    root_dir: str
    raw_data_path: str
    start_date: str
    end_date: str

    def __post_init__(self):
        # Convert start_date and end_date from string to datetime.date if needed
        self.start_date = self.convert_to_date(self.start_date)
        self.end_date = self.convert_to_date(self.end_date)

    def convert_to_date(self, date_str: str) -> Optional[datetime]:
        try:
            # Parse date string to datetime object, adjust format as needed
            return datetime.strptime(date_str, "%Y-%m-%d").date() if date_str else None
        except ValueError:
            # Handle invalid date format gracefully
            print(f"Warning: Invalid date format for '{date_str}', using None.")
            return None
