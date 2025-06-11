# app.py
import streamlit as st
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt
from tensorflow.keras.models import load_model
from sklearn.preprocessing import MinMaxScaler

# Load the trained LSTM model
model = load_model('stock_price_lstm_model.keras')

st.title("📈 Stock Price Prediction App")

# Get user input
ticker = st.text_input("Enter Stock Ticker (e.g., AAPL)", "AAPL")
start_date = st.date_input("Start Date", value=pd.to_datetime("2015-01-01"))
end_date = st.date_input("End Date", value=pd.to_datetime("2023-12-31"))

if st.button("Predict"):
    df = yf.download(ticker, start=start_date, end=end_date)
    data = df[['Close']].copy()

    # Scale
    scaler = MinMaxScaler()
    scaled_data = scaler.fit_transform(data)

    # Prepare last 60 days for prediction
    last_60 = scaled_data[-60:]
    X_input = np.reshape(last_60, (1, 60, 1))

    # Predict next price
    pred_scaled = model.predict(X_input)
    pred = scaler.inverse_transform(pred_scaled)

    st.success(f"📊 Predicted next day closing price for {ticker}: ₹{round(pred[0][0], 2)}")

    # Plot the last prices
    st.subheader("📉 Last 60 Closing Prices")
    fig, ax = plt.subplots()
    ax.plot(data[-60:].index, data[-60:].values, label="Last 60 Days")
    ax.axhline(pred[0][0], color='red', linestyle='--', label="Predicted Next Price")
    ax.legend()
    st.pyplot(fig)
