import numpy as np
import yfinance as yf
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression

class StockPredictor:
    def __init__(self, symbol):
        self.symbol = symbol
        self.model = LinearRegression()
        self.scaler = StandardScaler()

    def train_model(self):
        print("Training model...")
        
        # Fetch historical stock data
        data = yf.download(self.symbol, period="6mo", interval="1d")  # 6 months of data
        if data.empty:
            raise ValueError("No data found for the given stock symbol.")
        
        # Use only closing prices
        data['Date'] = data.index
        data['Date'] = data['Date'].map(lambda x: x.toordinal())  # Convert dates to ordinal values
        X = data[['Date']].values
        y = data['Close'].values

        # Scale the data
        self.scaler.fit(X)  # ✅ Fit the scaler here
        X_scaled = self.scaler.transform(X)

        # Train the model
        self.model.fit(X_scaled, y)
        print("Model trained successfully!")

    def predict_next_day(self):
        # Predict for the next day's date
        latest_date = yf.download(self.symbol, period="1d", interval="1d").index[-1].toordinal() + 1
        latest_date_scaled = self.scaler.transform([[latest_date]])  # ✅ Transform correctly
        predicted_price = self.model.predict(latest_date_scaled)

        return float(predicted_price)  # Ensure the result is JSON serializable
