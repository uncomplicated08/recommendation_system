# test.py

import numpy as np
from scipy.sparse import csr_matrix
from implicit.als import AlternatingLeastSquares

# Generate synthetic data
data = np.random.rand(10, 10)  # Small dataset
data[data < 0.8] = 0  # Sparsify the data
user_item_matrix = csr_matrix(data)
user_items = user_item_matrix.T.tocsr()  # Transposing to get items-users matrix

# Initialize and train model
model = AlternatingLeastSquares(factors=2, regularization=0.1, iterations=5)
model.fit(user_item_matrix)

# Attempt to get recommendations for a user
print(f"User items matrix shape: {user_items.shape}")
print(f"User row contents for user_id=0: {user_items[:, 0].toarray()}")

try:
    recommendations = model.recommend(0, user_items, N=3)
    print("Synthetic data recommendations:", recommendations)
except Exception as e:
    print("Error with synthetic data:", str(e))
