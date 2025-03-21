# Car Price Prediction Model

This repository contains a machine learning model for predicting car prices based on various features such as mileage, age, brand, engine type, and more. The model is built using Python and popular machine learning libraries like Scikit-learn, Pandas, Streamlit and NumPy.

## Table of Contents
- [Overview](#overview)
- [Dataset](#dataset)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Model Performance](#model-performance)
- [Working Prototype](#working-prototype)
- [Contributing](#contributing)
- [License](#license)

---

## Overview
The goal of this project is to predict the price of a car based on its features. This can be useful for buyers, sellers, and dealerships to estimate the fair market value of a vehicle. The model is trained on a dataset containing historical car prices and their corresponding features.

---

## Dataset
The dataset used for this project is sourced from [Kaggle](https://www.kaggle.com/) . It includes the following columns:
- **Car Name**: Name of the car.
- **Year**: Manufacturing year of the car.
- **Selling Price**: Target variable (price of the car).
- **Present Price**: Current showroom price.
- **Kms Driven**: Total kilometers driven.
- **Fuel Type**: Type of fuel (Petrol, Diesel, Electric, etc.).
- **Seller Type**: Type of seller (Individual or Dealer).
- **Transmission**: Transmission type (Manual or Automatic).
- **Owner**: Number of previous owners.

---

## Features
The following features are used to train the model:
- Numerical Features: Year, Present Price, Kms Driven, Owner.
- Categorical Features: Fuel Type, Seller Type, Transmission.

---

## Installation
To run this project locally, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/car-price-prediction.git
   cd car-price-prediction
   ```

2. **Set up a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage
1. **Train the model:**
   Run the training script to train the model on the dataset:
   ```bash
   python train.py
   ```

2. **Make predictions:**
   Use the trained model to predict car prices:
   ```bash
   python predict.py
   ```

3. **Explore the notebook:**
   You can also explore the Jupyter Notebook (`car_price_prediction.ipynb`) for a step-by-step explanation of the data preprocessing, model training, and evaluation.

---

## Model Performance
The model's performance is evaluated using the R² score:
- **Training R² Score:** 99.91%
- **Testing R² Score:** 99.96%

The model achieves excellent accuracy on both the training and testing datasets.

---

## Working Prototype
Here's a demo of the working prototype:






![Car Prediction Model Prototype](https://github.com/user-attachments/assets/3c9fb06b-f269-4957-bbc2-33bcde329386)



---

## Contributing
Contributions are welcome! If you'd like to contribute, please follow these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeatureName`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeatureName`).
5. Open a pull request.

---

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments
- Dataset sourced from [Kaggle](https://www.kaggle.com/).
- Thanks to the open-source community for providing helpful libraries and tools.

---
