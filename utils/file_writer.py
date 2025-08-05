import pandas as pd
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent.parent / "data"

def save_csv(df: pd.DataFrame, filename: str):
    """
    Save the DataFrame to a CSV file in the DATA_DIR directory.
    Args:
        df: The DataFrame to save.
        filename: The name of the CSV file (e.g., 'attendance.csv')
    """
    file_path = DATA_DIR / filename
    df.to_csv(file_path, index=False)
