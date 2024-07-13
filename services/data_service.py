# services/data_service.py

import pandas as pd
from pandas import DataFrame
from models.preprocess import prepare_data

def get_processed_data(filepath: str) -> DataFrame:
    """Interface to preprocess and load data for the recommendation system."""
    return prepare_data(filepath)
