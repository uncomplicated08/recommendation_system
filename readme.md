
# E-commerce Recommendation Engine

## Overview

This project is a simple yet effective recommendation engine designed for an e-commerce platform. It uses collaborative filtering to provide personalized product recommendations to users based on their browsing and purchase history.

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

## Setup Instructions

### Prerequisites

- Python 3.11.5 or higher
- Pip (Python package installer)
### Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/your-username/recommendation_system.git
   cd recommendation_system
   ```

2. **Create a Virtual Environment**:

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Prepare the Dataset**:
   
   Place your dataset file (`dataset.csv`) into the `data/` directory. Ensure it has the necessary columns like `user_id`, `product_id`, and `rating`.


### Additional Setup for Windows Users

If you encounter an error while installing the `surprise` package, you may need to install Microsoft Visual C++ 14.0 or greater. Follow these steps:

1. **Download and Install Microsoft C++ Build Tools**:

   - Go to the [Microsoft Visual C++ Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/) page.
   - Download the installer and run it.
   - During installation, select the "Development with C++" workload.

2. **Retry Installing the `surprise` Package**:

   ```bash
   pip install surprise
   ```

### Running the Project

1. **Train and Save the Recommendation Model**:

   Run the main script to preprocess the data, train the recommendation model, and save it.

   ```bash
   python main.py
   ```

   This will output the trained model and print the RMSE (Root Mean Square Error) of the model on the test dataset.

### Project Components

- **Data Preprocessing**: The `models/preprocess.py` script handles data loading and cleaning.
- **Model Training**: The `models/recommender.py` script builds and trains the recommendation model.
- **Services**: The `services/` directory contains scripts for handling data operations and interacting with the recommendation model.

### Future Work

- **GUI Development**: Build a graphical user interface to interact with the recommendation engine.
- **Model Optimization**: Explore and implement more advanced recommendation algorithms.
- **Scalability Improvements**: Optimize the system to handle larger datasets and more users.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Dataset provided by Dr. Daqing Chen, Director of the Public Analytics group at London South Bank University.
- [Surprise Library](https://surprise.readthedocs.io/) for building recommendation systems in Python.
