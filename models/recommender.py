# models/recommender.py

from sklearn.decomposition import TruncatedSVD
from scipy.sparse import csr_matrix
import pandas as pd
import numpy as np
import pickle


def build_model(df: pd.DataFrame, n_components=50):
    """Build and train a model using Truncated SVD for recommendation."""
    # Create a CSR matrix
    user_item_matrix = csr_matrix((df['rating'], (df['user_id'], df['product_id'])))
    
    # Initialize and train the model
    model = TruncatedSVD(n_components=n_components)
    model.fit(user_item_matrix)
    
    return model, user_item_matrix

def get_recommendations(model, user_item_matrix, user_id: int, n_recommendations: int = 5):
    """Generate recommendations for a given user."""
    user_projection = model.transform(user_item_matrix)
    item_projection = model.components_.T
    
    # Predict ratings for all items
    pred_ratings = np.dot(user_projection[user_id], item_projection.T)
    recommended_item_indices = np.argsort(-pred_ratings)[:n_recommendations]
    
    return recommended_item_indices

def save_model(model, filename='models/model.pkl'):
    """Save the trained model to a file."""
    with open(filename, 'wb') as f:
        pickle.dump(model, f)

def load_model(filename='models/model.pkl'):
    """Load a trained model from a file."""
    with open(filename, 'rb') as f:
        model = pickle.load(f)
    return model