# 🏡 House Price Predictor

A machine learning web application built using **Python**, **scikit-learn**, and **Streamlit** that predicts house prices based on key property features such as overall quality, living area, garage capacity, basement area, number of bathrooms, fireplaces, lot size, and year built.

The app displays the estimated house value in **USD** and **Indian Rupees (₹)**, making it useful for both global and Indian users.

---

## 🚀 Live Demo
🔗 https://house-price-predictorgit-qvjk6pdnk3vywt4ty7bbmv.streamlit.app/


## ✨ Features

- 📊 **ML Model**: Ridge Regression  
- 🧠 **Dataset**: Ames Housing Dataset (Kaggle)  
- 🎯 **Accuracy**: **R² ≈ 0.91**  
- 📈 **Two-currency Output**: USD & INR  
- ⚡ **Fast Real-time Predictions** via Streamlit  
- 🧮 Pre-trained model & scaler loaded from `.pkl` files

---

## 🧠 Machine Learning Workflow

### Dataset
Ames House Prices Dataset (Kaggle)

### Target Variable
`SalePrice`

### Steps Performed
- Exploratory Data Analysis (EDA)  
- Missing value handling  
- Outlier detection/removal  
- Ordinal + One-Hot Encoding  
- Log transformation of target  
- Feature scaling (`StandardScaler`)  
- Model comparison (Ridge, Lasso, RandomForest)  
- Saving best model (`joblib`)

### Best Model
**Ridge Regression** — chosen for stability and strong generalization.

---

## 🛠 Tech Stack

- **Python**  
- **Pandas**, **NumPy**  
- **scikit-learn**  
- **Streamlit**  
- **joblib** (model serialization)

---

## 📂 Project Structure

```bash
house-price-predictor/
├── app.py                   # Streamlit application
├── house_price_model.pkl    # Trained Ridge Regression model
├── scaler.pkl               # Fitted scaler used during training
├── requirements.txt         # Python dependencies
└── .streamlit/
    └── config.toml          # Theme configuration (light mode)
```

---

## 🚀 Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/Sakets71/house-price-predictor.git
cd house-price-predictor

```

### 2. Create & activate a virtual environment

**Windows**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS / Linux**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the app

```bash
streamlit run app.py
```

Open the local URL shown (usually `http://localhost:8501`).

---

## 📌 Notes for Deployment (Streamlit Cloud)

- Ensure `requirements.txt` includes at least:

  ```txt
  streamlit
  scikit-learn
  joblib
  numpy
  pandas
  ```

- Place `house_price_model.pkl` and `scaler.pkl` in the repo root (same directory as `app.py`).

- Add `.streamlit/config.toml` to force light theme:

  ```toml
  [theme]
  base="light"
  primaryColor="#4B5C5C"
  backgroundColor="#F1F1F1"
  secondaryBackgroundColor="#FAFAFA"
  textColor="#000000"
  ```

---

## 📊 Output Example

- **₹ Estimated House Value in INR** (converted using a fixed USD→INR rate set in `app.py`)  
- **$ Estimated House Value in USD**  
- **Model Accuracy (R² Score): 0.91**

---

## 🔧 Future Improvements

- Add more dataset features (Neighborhood, HouseStyle, YearRemodAdd)  
- Show feature importance / SHAP explanations  
- Add download-as-PDF prediction report  
- Add historical price trend visualization  
- Add user authentication & saving predictions  

---

## 👤 Author

**Saket Surywanshi**  
Machine Learning & Software Development Enthusiast  
GitHub: https://github.com/Sakets71  

---

## ⭐ If you found this useful

Please star the repository to support the project! ⭐
