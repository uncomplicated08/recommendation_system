# main.py

import pandas as pd
from models.recommender import build_model, get_recommendations, save_model, load_model

if __name__ == "__main__":
    data_filepath = "data/dataset.csv"
    
    # Load data
    df = pd.read_csv(data_filepath)
    df.dropna(subset=['CustomerID', 'StockCode', 'Quantity'], inplace=True)  # Ensure no key info is missing
    
    # Assuming Quantity can represent preference and only positive quantities are valid for recommendations
    df = df[df['Quantity'] > 0]
    df['rating'] = df['Quantity'].astype(float)  # Assign 'rating' before any further data manipulation

    # Extract unique products for mapping recommendations back to product codes
    unique_products = df[['StockCode', 'Description']].drop_duplicates().reset_index(drop=True)
    unique_products['product_id'] = pd.factorize(unique_products['StockCode'])[0]  # Correct context for factorization

    # Factorize user and product IDs for the model
    df['user_id'] = pd.factorize(df['CustomerID'])[0]
    df['product_id'] = pd.factorize(df['StockCode'])[0]

    # Build the model
    model, user_item_matrix = build_model(df)
    save_model(model)  # Save the model after training
    
    # Load the model back
    model = load_model()
    
    # Get recommendations for user with index 0
    recommendations = get_recommendations(model, user_item_matrix, user_id=0)
    recommended_products = unique_products.loc[unique_products['product_id'].isin(recommendations)]
    
    print("Recommendations for user 0:")
    print(recommended_products[['StockCode', 'Description']])