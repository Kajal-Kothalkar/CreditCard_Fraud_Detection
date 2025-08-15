# 💳 Credit Card Fraud Detection App

[🔗 View Project Preview](preview.jpg)

A **Streamlit-based web application** that detects fraudulent credit card transactions using a pre-trained machine learning model.  
The app takes in **30 transaction features** and predicts whether a transaction is **fraudulent** or **legitimate**.

---

## 📋 Features
- **User-friendly interface** built with Streamlit.
- Accepts **30 numerical inputs** (Time, V1–V28, Amount).
- Real-time fraud prediction using a **Random Forest Classifier**.
- Displays prediction probability and clear fraud/legitimate indicators.

---

## 🛠 Tools & Technologies
- **Python 3.x**
- **Streamlit** – Interactive UI
- **NumPy** – Data handling
- **Joblib** – Model loading
- **scikit-learn** – Machine learning model and scaling

---

## 📦 Requirements
- Python **3.8+**
- pip package manager
- Installed dependencies from `requirements.txt`

  📂 Project Structure
├── app.py               # Streamlit app entry point
├── rf_model.pkl         # Trained Random Forest model
├── scaler.pkl           # Scaler used for feature normalization
├── preview.jpg          # Application preview image
├── requirements.txt     # Dependencies
└── README.md            # Project documentation


Install dependencies:
```bash
pip install -r requirements.txt

📂 Project Structure
├── app.py               # Streamlit app entry point
├── rf_model.pkl         # Trained Random Forest model
├── scaler.pkl           # Scaler used for feature normalization
├── preview.jpg          # Application preview image
├── requirements.txt     # Dependencies
└── README.md            # Project documentation
