# gui/main_window.py
import sys
import os

# Add the parent directory of recommendation_system to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QTextEdit, QVBoxLayout, QWidget
from models.recommender import load_recommendation_system, get_recommendations
from models.preprocess import load_and_preprocess_data, extract_unique_products


import pandas as pd

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Load the model, user-item matrix, and unique products
        self.model, self.user_item_matrix, self.unique_products = load_recommendation_system()
        self.df = load_and_preprocess_data('data/dataset.csv')

        # Setup the layout
        layout = QVBoxLayout()

        # User ID input
        self.user_input = QLineEdit(self)
        self.user_input.setPlaceholderText("Enter user ID...")
        layout.addWidget(self.user_input)

        # Button to get recommendations
        self.button = QPushButton('Get Recommendations', self)
        self.button.clicked.connect(self.display_recommendations)
        layout.addWidget(self.button)

        # Text edit for displaying recommendations
        self.text_edit = QTextEdit(self)
        self.text_edit.setPlaceholderText("Recommendations will appear here...")
        layout.addWidget(self.text_edit)

        # Set the central widget and layout
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.setWindowTitle("Recommendation System")
        self.setGeometry(100, 100, 400, 300)

    def display_recommendations(self):
        user_id = int(self.user_input.text())
        recommendations = get_recommendations(self.model, self.user_item_matrix, user_id)
        self.text_edit.clear()
        self.text_edit.append("Recommendations for user {}: \n".format(user_id))
        for idx in recommendations:
            product = self.unique_products.loc[self.unique_products['product_id'] == idx, 'Description'].values[0]
            self.text_edit.append(product)

# Setup and run the application
if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
