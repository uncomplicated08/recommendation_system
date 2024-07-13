# services/recommendation_service.py

import pandas as pd
from implicit.als import AlternatingLeastSquares
from models.recommender import build_model, save_model
from services.data_service import get_processed_data

def create_and_save_model(data_filepath: str, model_filepath: str) -> None:
    """Create, train, and save the recommendation model."""
    df: pd.DataFrame = get_processed_data(data_filepath)
    model: AlternatingLeastSquares = build_model(df)
    save_model(model, model_filepath)
