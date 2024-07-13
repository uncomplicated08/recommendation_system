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

def save_recommendation_system(model, user_item_matrix, unique_products, filename='models/model.pkl'):
    """Save the trained model, user-item matrix, and unique products to a file."""
    with open(filename, 'wb') as f:
        pickle.dump({'model': model, 'user_item_matrix': user_item_matrix, 'unique_products': unique_products}, f)

def load_recommendation_system(filename='models/model.pkl'):
    """Load a trained model, user-item matrix, and unique products from a file."""
    with open(filename, 'rb') as f:
        data = pickle.load(f)
    return data['model'], data['user_item_matrix'], data['unique_products']