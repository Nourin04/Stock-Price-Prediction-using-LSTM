

# 📈 Stock Price Predictor with LSTM

Predict the **next day's stock closing price** using a deep learning model built with **LSTM (Long Short-Term Memory)** networks. This project features an intuitive **Gradio-based interface** and can be deployed locally or on **Hugging Face Spaces**.

---

## 🚀 Demo

🌐 Live Demo: [Try it on Hugging Face Spaces](https://huggingface.co/spaces/noureenac/stock-predictor)

![image](https://github.com/user-attachments/assets/6d21e82a-f62e-418c-bf4a-43c67dd1870f)
![image](https://github.com/user-attachments/assets/07d70cfa-6327-40b9-b1f6-d7c7987dd870)

---

## 🧠 Project Overview

This application predicts the **next-day stock price** by learning patterns from the **past 60 days** of closing prices. It is built using:

* 📊 Time Series Forecasting
* 🔁 LSTM Neural Network
* 🧪 Scikit-learn for data preprocessing
* 🌐 Gradio for UI
* ☁️ Hugging Face for free public deployment

---

## 💼 Use Cases

* 📈 Investors exploring price trends
* 🎓 Students learning time-series forecasting
* ⚙️ Developers prototyping financial ML tools
* 🧪 Researchers benchmarking LSTM models

---

## 🗂️ Project Structure

```bash
Stock_Price_Predictor_App/
├── app.py                    # Main Gradio interface script
├── stock_price_lstm_model.keras  # Trained LSTM model
├── scaler.save              # Pre-fitted MinMaxScaler
├── requirements.txt         # Dependencies
└── README.md                # This documentation
```


---

## 📦 Requirements

Key packages used:

* `tensorflow`
* `scikit-learn`
* `gradio`
* `numpy`
* `joblib`

Ensure compatibility of TensorFlow with your Python version (preferably Python 3.10).

---

## 📌 Features

✅ Trained LSTM model
✅ Gradio web interface
✅ Scaler included for input normalization
✅ Clear and formatted output
✅ Hugging Face Spaces compatible

---

## 📊 Sample Input Format

```
231.3, 232.5, 233.1, ..., 245.8  # (Total 60 comma-separated values)
```

⚠️ Please enter exactly **60 values**, each representing the stock’s closing price for the last 60 trading days.

---

## 🔮 Output Example

```
📈 Predicted next day price: ₹246.89
```


---

## 🧠 Next Steps

* [ ] Auto-fetch prices using `yfinance`
* [ ] Dropdown menu for selecting companies
* [ ] Graph output using `matplotlib`
* [ ] Evaluation metrics (RMSE, MAE, etc.)

---

## 📚 License

This project is open-source under the [MIT License](LICENSE).

