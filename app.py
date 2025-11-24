import streamlit as st
import joblib
import numpy as np

# ========================================================================
# Streamlit Page Config
# ========================================================================
st.set_page_config(
    page_title="House Price Predictor",
    page_icon="🏡",
    layout="centered",
)

# ========================================================================
# Custom CSS (Matches config.toml theme)
# ========================================================================
st.markdown("""
<style>
    body {
        background-color: #F1F1F1;
        color: #000000;
        font-family: 'Inter', sans-serif;
    }

    .main-title {
        font-size: 2rem;
        font-weight: 700;
        color: #4B5C5C;
        text-align: center;
        margin-bottom: 0.5rem;
    }

    .sub-text {
        text-align: center;
        color: #444444;
        margin-bottom: 1.8rem;
        font-size: 1rem;
    }

    .card {
        background: #FAFAFA;
        padding: 1.5rem;
        border-radius: 0.75rem;
        box-shadow: 0 2px 6px rgba(0,0,0,0.08);
        border: 1px solid #d6d6d6;
    }

    .result-box {
        background: #4B5C5C;
        color: white;
        padding: 1.5rem;
        border-radius: 0.75rem;
        text-align: center;
        margin-top: 1.2rem;
    }

    .result-box h1 {
        font-size: 2rem;
        font-weight: 700;
    }

    .price-subtext {
        font-size: 0.9rem;
        margin-top: -6px;
        color: #f0f0f0;
    }

    .accuracy-box {
        background: #a1abce;
        color: black;
        padding: 1rem;
        border-radius: 0.5rem;
        text-align: center;
        margin-top: 1rem;
        font-weight: 600;
    }

    .stButton > button {
        background-color: #4B5C5C;
        color: white;
        border: none;
        padding: 0.75rem;
        border-radius: 0.5rem;
        font-weight: 600;
        width: 100%;
        font-size: 1rem;
    }

    .stButton > button:hover {
        background-color: #e62626;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# ========================================================================
# Load Model + Scaler
# ========================================================================
model = joblib.load(r"D:\\python\\EDA\\House Price\\house_price_model.pkl")
scaler = joblib.load(r"D:\\python\\EDA\\House Price\\scaler.pkl")

# ========================================================================
# Header Section
# ========================================================================
st.markdown("<div class='main-title'>House Price Predictor</div>", unsafe_allow_html=True)
st.markdown("<p class='sub-text'>Enter property details below and get valuation in USD & INR.</p>", unsafe_allow_html=True)

# ========================================================================
# Input Card
# ========================================================================
st.markdown("<div class='card'>", unsafe_allow_html=True)

st.subheader("Property Details")

OverallQual = st.slider("Overall Quality (1–10)", 1, 10, 7)
GrLivArea = st.number_input("Above Ground Living Area (sq ft)", 300, 8000, 1800)
GarageCars = st.slider("Garage Capacity", 0, 5, 2)
TotalBsmtSF = st.number_input("Basement Area (sq ft)", 0, 4000, 800)
YearBuilt = st.number_input("Year Built", 1800, 2025, 2005)
FullBath = st.slider("Full Bathrooms", 0, 5, 2)
Fireplaces = st.slider("Fireplaces", 0, 4, 1)
LotArea = st.number_input("Lot Area (sq ft)", 500, 80000, 10000)

st.markdown("</div>", unsafe_allow_html=True)

# ========================================================================
# Prediction Button
# ========================================================================
predict = st.button("Predict Price")

# ========================================================================
# Prediction Logic
# ========================================================================
if predict:
    input_data = np.array([[OverallQual, GrLivArea, GarageCars, TotalBsmtSF,
                            YearBuilt, FullBath, Fireplaces, LotArea]])

    scaled = scaler.transform(input_data)
    pred_log = model.predict(scaled)
    predicted_price_usd = float(np.expm1(pred_log)[0])

    # Convert USD to INR (fix conversion rate)
    USD_TO_INR = 83.0
    predicted_price_inr = predicted_price_usd * USD_TO_INR

    # Result Box (USD + INR)
    st.markdown(f"""
        <div class='result-box'>
            <h3>Estimated House Value</h3>
            <h1>₹{predicted_price_inr:,.0f}</h1>
            <p class='price-subtext'>Indian Rupees (INR)</p>
            <br>
            <h3 style='margin-top:10px;'>${predicted_price_usd:,.0f}</h3>
            <p class='price-subtext'>US Dollars (USD)</p>
        </div>
    """, unsafe_allow_html=True)

    # Accuracy Box
    st.markdown("""
        <div class='accuracy-box'>
            Model Accuracy (R² Score): <b>0.91</b>
        </div>
    """, unsafe_allow_html=True)
