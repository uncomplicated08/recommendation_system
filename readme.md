
# Recommendation System

This project implements an AI-powered recommendation engine for an e-commerce platform, providing personalized product recommendations based on user browsing and purchase history.

## Requirements

- Python 3.x
- Pandas
- NumPy
- Scikit-learn
- PyQt5

## Setup

1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd recommendation_system
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Place your dataset in the `data/` directory:
   ```plaintext
   recommendation_system/
   ├── data/
   │   └── dataset.csv
   ```

## Dataset

The dataset used in this project is the [Online Retail Transaction Data](https://www.kaggle.com/datasets/thedevastator/online-retail-transaction-data?resource=download) from Kaggle. 

This data set provides an in-depth look at transactions, product details, and customer information documented by an online retail company based in the UK. The scope of the data spans vastly, from granular details about each product sold to extensive customer data sets from different countries.


## Running the Recommendation Engine

1. To preprocess the data, train the model, and get recommendations:
   ```bash
   python main.py
   ```

2. To run the GUI for interactive recommendations:
   ```bash
   python gui/main_window.py
   ```

## Project Structure

```
recommendation_system/
│
├── README.md
├── requirements.txt
├── main.py
│
├── data/
│   └── dataset.csv           # Store the dataset file or data extraction scripts here
│
├── models/
│   ├── __init__.py
│   ├── recommender.py        # Contains the recommendation logic and model training
│   └── preprocess.py         # Data cleaning and preprocessing functions
│
├── services/
│   ├── __init__.py
│   ├── data_service.py       # Service to handle data operations
│   └── recommendation_service.py # Service to interact with the recommendation model
│
├── gui/
│   ├── __init__.py
│   └── main_window.py        # GUI components for interacting with the recommendation system
│
└── utils/
    ├── __init__.py
    └── helpers.py            # Helper functions that might be used across the project
```

## Contributing

Feel free to submit issues or pull requests if you have any suggestions or improvements.