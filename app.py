import requests
import numpy as np
import pandas as pd
import streamlit as st

# Title
st.title("Binance Daily Return Predictor")
st.markdown("Predict the **probability of a gain** for a cryptocurrency using technical indicators.")

# Sidebar input fields
st.sidebar.header("Input Features")

open_price = st.sidebar.number_input("Open Price", min_value=0.0, value=100.0)
high_price = st.sidebar.number_input("High Price", min_value=0.0, value=110.0)
low_price = st.sidebar.number_input("Low Price", min_value=0.0, value=90.0)
close_price = st.sidebar.number_input("Close Price", min_value=0.0, value=105.0)
volume = st.sidebar.number_input("Volume", min_value=0.0, value=100000.0)
volatility = st.sidebar.number_input("Volatility", min_value=0.0, value=0.05)
ma_7 = st.sidebar.number_input("7-day Moving Average", min_value=0.0, value=102.0)
ma_30 = st.sidebar.number_input("30-day Moving Average", min_value=0.0, value=98.0)
cumulative_return = st.sidebar.number_input("Cumulative Return", min_value=-1.0, max_value=1.0, value=0.1)

# Combine all inputs into feature vector
features = [
    open_price, high_price, low_price, close_price, volume,
    volatility, ma_7, ma_30, cumulative_return
]

# Simulated prediction (placeholder logic)
predicted_return = np.dot(features, np.random.rand(len(features)))  # To be replaced

# Uncomment below when backend is ready
try:
    response = requests.post("http://localhost:5000/predict", json={"features": features})
    response.raise_for_status()
    predicted_return = response.json().get("positive_return_probability", 0)
except Exception as e:
    st.error(f"Prediction failed: {e}")
    predicted_return = 0

# Show prediction
st.markdown("### Probability of Positive Daily Return")
st.success(f"{predicted_return:.2%}")  # Shows as percentage (e.g., 76.34%)

# Binary classification result
if predicted_return >= 0.5:
    st.info("🔼 **Expected: Gain**")
else:
    st.warning("🔽 **Expected: Loss**")

# Optional: Show feature inputs
if st.checkbox("Show input features"):
    display_data = {
        "open": open_price,
        "high": high_price,
        "low": low_price,
        "close": close_price,
        "volume": volume,
        "volatility": volatility,
        "ma_7": ma_7,
        "ma_30": ma_30,
        "cumulative_return": cumulative_return,
    }
    input_df = pd.DataFrame([display_data])
    st.dataframe(input_df)

