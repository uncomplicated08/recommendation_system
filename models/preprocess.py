# models/preprocess.py

import pandas as pd
from pandas import DataFrame

def load_data(filepath: str) -> DataFrame:
    """Load dataset into a pandas DataFrame."""
    df = pd.read_csv(filepath)
    print(f"Columns in the dataset: {df.columns.tolist()}")
    return df

def clean_data(df: DataFrame) -> DataFrame:
    """Clean the data by removing duplicates, handling missing values, etc."""
    df.drop_duplicates(inplace=True)
    df.dropna(subset=['CustomerID', 'StockCode'], inplace=True)  # Ensure we have user and product information
    return df

def prepare_data(filepath: str) -> DataFrame:
    """Prepare data by loading, cleaning, and transforming it."""
    df = load_data(filepath)
    df = clean_data(df)
    
    # Create necessary columns
    df['user_id'] = df['CustomerID'].astype(int)
    df['product_id'] = df['StockCode'].astype(str)
    df['rating'] = df['Quantity'].astype(float)  # Using Quantity as a proxy for rating
    
    # Create integer mappings for user_id and product_id
    user_id_mapping = {id: idx for idx, id in enumerate(df['user_id'].unique())}
    product_id_mapping = {id: idx for idx, id in enumerate(df['product_id'].unique())}
    
    df['user_id'] = df['user_id'].map(user_id_mapping)
    df['product_id'] = df['product_id'].map(product_id_mapping)
    
    return df[['user_id', 'product_id', 'rating']]



def load_and_preprocess_data(filepath: str) -> pd.DataFrame:
    # Load data
    df = pd.read_csv(filepath)
    
    # Ensure no key info is missing
    df.dropna(subset=['CustomerID', 'StockCode', 'Quantity'], inplace=True)
    
    # Convert 'InvoiceNo' to numeric, handling errors by setting them to NaN
    df['InvoiceNo'] = pd.to_numeric(df['InvoiceNo'], errors='coerce')
    
    # Drop rows where 'InvoiceNo' could not be converted to numeric
    df.dropna(subset=['InvoiceNo'], inplace=True)
    
    # Ensure positive quantities
    df = df[df['Quantity'] > 0]
    
    # Assign 'rating' before any further data manipulation
    df['rating'] = df['Quantity'].astype(float)
    
    # Factorize user and product IDs for the model
    df['user_id'] = pd.factorize(df['CustomerID'])[0]
    df['product_id'] = pd.factorize(df['StockCode'])[0]
    
    return df

def extract_unique_products(df: pd.DataFrame) -> pd.DataFrame:
    unique_products = df[['StockCode', 'Description']].drop_duplicates().reset_index(drop=True)
    unique_products['product_id'] = pd.factorize(unique_products['StockCode'])[0]  # Correct context for factorization
    return unique_products