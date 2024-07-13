# main.py

import pandas as pd
from models.recommender import build_model, get_recommendations, save_recommendation_system, load_recommendation_system
from models.preprocess import load_and_preprocess_data, extract_unique_products

if __name__ == "__main__":
    data_filepath = "data/dataset.csv"
    
    # Load and preprocess data
    df = load_and_preprocess_data(data_filepath)
    
    # Extract unique products for mapping recommendations back to product codes
    unique_products = extract_unique_products(df)
    

    # Build the model
    model, user_item_matrix = build_model(df)
    save_recommendation_system(model, user_item_matrix, unique_products)  # Save the model, matrix, and unique products
    
    # Load the model, matrix, and unique products back
    model, user_item_matrix, unique_products = load_recommendation_system()
  
    # Get recommendations for user with index 0
    recommendations = get_recommendations(model, user_item_matrix, user_id=0)
    recommended_products = unique_products.loc[unique_products['product_id'].isin(recommendations)]
    
    print("Recommendations for user 0:")
    print(recommended_products[['StockCode', 'Description']])