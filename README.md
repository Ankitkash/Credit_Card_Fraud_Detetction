# 💳 Credit Card Fraud Detection using Machine Learning

## 📌 Project Overview

This project focuses on detecting fraudulent credit card transactions using Machine Learning classification techniques.

Credit card fraud detection is a critical problem in the financial industry because fraudulent transactions are very rare compared to genuine ones. Therefore, special attention was given to handling class imbalance and improving recall for the fraud class.

This project covers the complete Machine Learning lifecycle:

- Data Preprocessing  
- Exploratory Data Analysis (EDA)  
- Feature Engineering  
- Model Training  
- Model Evaluation  
- Model Deployment using Streamlit  

---

## 📂 Project Structure

```
Credit-Card-Fraud-Detection/
│
├── app.py                                # Streamlit web application
├── credit_card_fraud_detection_model.pkl # Trained ML model
├── Credit_Card_Fraud_Detection.ipynb     # Jupyter notebook (EDA + Model training)
├── requirements.txt                      # Required Python libraries
```

---

## 🛠️ Tech Stack

- Python  
- Pandas  
- NumPy  
- Scikit-learn  
- Matplotlib  
- Seaborn  
- Streamlit  

---

## 📊 Dataset Information

The dataset used for this project is the Credit Card Fraud Detection dataset.

### Dataset Features:

- V1 to V28 → PCA transformed features  
- Time → Time elapsed between transactions  
- Amount → Transaction amount  
- Class → Target variable  
  - 0 → Genuine Transaction  
  - 1 → Fraudulent Transaction  

⚠ The dataset is highly imbalanced, with fraud cases representing a very small percentage of total transactions.

---

## 🔍 Exploratory Data Analysis (EDA)

The following analysis was performed:

- Checked class distribution  
- Visualized fraud vs non-fraud transactions  
- Distribution of transaction amounts  
- Identified imbalance in target variable  

---

## ⚙️ Data Preprocessing

- Checked for missing values  
- Feature scaling applied  
- Selected relevant features  
- Handled class imbalance  
- Split dataset into training and testing sets  

---

## 🤖 Model Building

The model development process included:

1. Train-Test Split  
2. Model Training using classification algorithm  
3. Model Evaluation using:
   - Accuracy  
   - Precision  
   - Recall  
   - F1-Score  
   - Confusion Matrix  

Since fraud detection is a sensitive problem, Recall was prioritized to minimize false negatives (undetected fraud transactions).

---

## 📈 Model Performance

(Add your actual metrics below)

```
Accuracy  : 99.2%
Precision : 91%
Recall    : 87%
F1-Score  : 89%
```

---

## 🌐 Streamlit Web Application

A simple and interactive web application was developed using Streamlit.

### Features of the App:

- User can enter transaction details  
- Click on Predict  
- Instantly see whether the transaction is:
  - Fraudulent  
  - Genuine  

---

