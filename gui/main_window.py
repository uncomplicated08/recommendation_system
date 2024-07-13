# gui/main_window.py
import sys
import os

# Add the parent directory of recommendation_system to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QComboBox, QTextEdit, QVBoxLayout, QHBoxLayout, QWidget, QLabel
from models.recommender import load_recommendation_system, get_recommendations
from models.preprocess import load_and_preprocess_data

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Load the model, user-item matrix, and unique products
        self.model, self.user_item_matrix, self.unique_products = load_recommendation_system()
        self.df = load_and_preprocess_data('data/dataset.csv')

        # Setup the layout
        main_layout = QVBoxLayout()

        # Horizontal layout for dropdowns
        dropdown_layout = QHBoxLayout()

        # User ID dropdown
        self.user_dropdown = QComboBox(self)
        # Create a mapping of user_id to CustomerID
        user_customer_mapping = self.df[['user_id', 'CustomerID']].drop_duplicates()
        user_customer_mapping['display'] = user_customer_mapping.apply(lambda x: f"CUSTOMER: {x['CustomerID']} (user_id: {x['user_id']})", axis=1)
        for _, row in user_customer_mapping.iterrows():
            self.user_dropdown.addItem(row['display'], row['user_id'])
        dropdown_layout.addWidget(QLabel("Select User:"))
        dropdown_layout.addWidget(self.user_dropdown)

        # Number of recommendations dropdown
        self.recommendations_dropdown = QComboBox(self)
        for i in range(2, 11):
            self.recommendations_dropdown.addItem(str(i))
        dropdown_layout.addWidget(QLabel("Number of Recommendations:"))
        dropdown_layout.addWidget(self.recommendations_dropdown)

        main_layout.addLayout(dropdown_layout)

        # Button to get recommendations
        self.button = QPushButton('Get Recommendations', self)
        self.button.clicked.connect(self.display_recommendations)
        main_layout.addWidget(self.button)

        # Text edit for displaying recommendations
        self.text_edit = QTextEdit(self)
        self.text_edit.setPlaceholderText("Recommendations will appear here...")
        main_layout.addWidget(self.text_edit)

        # Set the central widget and layout
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

        self.setWindowTitle("Recommendation System")
        self.setGeometry(100, 100, 400, 300)

    def display_recommendations(self):
        user_id = self.user_dropdown.currentData()
        num_recommendations = int(self.recommendations_dropdown.currentText())
        customer_id = self.df.loc[self.df['user_id'] == user_id, 'CustomerID'].values[0]
        recommendations = get_recommendations(self.model, self.user_item_matrix, user_id, n_recommendations=num_recommendations)
        self.text_edit.clear()
        self.text_edit.append(f"Recommendations for Customer ID {customer_id} (user_id: {user_id}): \n")
        for idx in recommendations:
            product = self.unique_products.loc[self.unique_products['product_id'] == idx, 'Description'].values[0]
            self.text_edit.append(product)

# Setup and run the application
if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
