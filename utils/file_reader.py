import pandas as pd
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent.parent / "data"

def read_csv(filename: str) -> str:
    """
    Read a CSV file and returns the pandas dataframe of that csv.

    Args:
        filename: Name of the CSV file (e.g. 'sample.csv')

    Returns:
        A pandas dataframe object.
    """
    file_path = DATA_DIR / filename
    df = pd.read_csv(file_path)
    return df
