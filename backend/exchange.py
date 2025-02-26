# import yfinance as yf
# import pandas as pd
# import matplotlib.pyplot as plt
# import requests

# # Dictionary of stock symbols
# stock_symbols = {
#     "Apple": "AAPL", "Microsoft": "MSFT", "Amazon": "AMZN", "Tesla": "TSLA",
#     "Google (Alphabet)": "GOOGL", "Meta (Facebook)": "META", "Nvidia": "NVDA",
#     "Netflix": "NFLX", "Intel": "INTC", "AMD": "AMD", "Qualcomm": "QCOM",
# }

# # Function to fetch exchange rates
# def fetch_exchange_rate(target_currency, base_currency="USD"):
#     url = f"https://open.er-api.com/v6/latest/{base_currency}"
#     response = requests.get(url)

#     if response.status_code == 200:
#         data = response.json()
#         if data.get("result") == "success":
#             rates = data["rates"]
#             return rates.get(target_currency)
#         else:
#             print(f"❌ API Error: {data.get('error-type', 'Unknown Error')}")
#     else:
#         print(f"❌ HTTP Error: {response.status_code}")

#     return None

# # Function to convert stock prices
# def convert_prices(data, exchange_rate):
#     if exchange_rate:
#         data["Close"] = data["Close"] * exchange_rate
#         return data
#     else:
#         print("❌ Failed to fetch exchange rate.")
#         return data

# # Get stock selection
# print("\n📌 Available Stocks:")
# for company in stock_symbols.keys():
#     print(f"- {company}")

# company_name = input("\nEnter the company name (e.g., 'Apple', 'Tesla'): ").strip()
# ticker = stock_symbols.get(company_name)

# if not ticker:
#     print("\n❌ Invalid company name! Exiting.")
#     exit()

# # Fetch stock data
# print(f"\n✅ Fetching stock data for {company_name} ({ticker})...")
# stock_data = yf.download(ticker, period="5y")

# # Handle missing values
# stock_data.ffill(inplace=True)

# # Get target currency
# target_currency = input("\n🌍 Enter target currency (e.g., 'INR', 'EUR'): ").strip().upper()

# # Fetch and apply exchange rate
# exchange_rate = fetch_exchange_rate(target_currency)
# if exchange_rate:
#     stock_data = convert_prices(stock_data, exchange_rate)
#     print(f"💱 Exchange Rate: 1 USD = {exchange_rate:.2f} {target_currency}")

# # Plot Stock Price
# plt.figure(figsize=(12, 6))
# plt.plot(stock_data["Close"], label=f"Stock Price ({target_currency})", color='blue')
# plt.title(f"{company_name} Stock Price ({target_currency})")
# plt.xlabel("Date")
# plt.ylabel(f"Price in {target_currency}")
# plt.legend()
# plt.grid(True)
# plt.show()
## Phase 4 starts
"""
✅ 1. Currency Conversion (USD to INR & vice versa)
Allow users to view stock prices in both USD and INR.
Approach Options:
    Static Conversion Rate (Fixed rate like 1 USD = 83 INR).
    Live Exchange Rate (Fetch real-time rates via an API).

✅ 2. Moving from CLI to an Interactive Dashboard
    Upgrade from a text-based interface to a simple web-based dashboard.
    Technology: Flask + React + Tailwind CSS (as planned earlier).
    Display graphs interactively instead of just static Matplotlib plots.

✅ 3. Enhancing Stock Predictions
    Incorporate a basic prediction model for future stock trends.
    Implement Linear Regression / Time Series Forecasting (like ARIMA, LSTM).
    Compare actual vs predicted stock movements.

✅ 4. More Data Insights & Export Options
    Allow users to export stock data & indicators in CSV/Excel.
    Add summary statistics like max, min, volatility, CAGR, etc.
    Improve visualization with interactive plots (Plotly).

✅ 5. Adding More Technical Indicators
  Add popular indicators like:
    Bollinger Bands 📊
    Stochastic Oscillator 📈
    VWAP (Volume Weighted Average Price)

✅ 6. User Input Enhancements
    Let users select custom timeframes (1Y, 5Y, max, custom range).
    Improve error handling for invalid stock selections.

"""

import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from forex_python.converter import CurrencyRates
import requests

# Initialize forex-python currency converter
c = CurrencyRates()


# Dictionary of common stock symbols
stock_symbols = {
    "Apple": "AAPL", "Microsoft": "MSFT", "Amazon": "AMZN", "Tesla": "TSLA",
    "Google (Alphabet)": "GOOGL", "Meta (Facebook)": "META", "Nvidia": "NVDA",
    "Netflix": "NFLX", "Intel": "INTC", "AMD": "AMD", "Qualcomm": "QCOM",
    "Cisco Systems": "CSCO", "IBM": "IBM", "Oracle": "ORCL", "Salesforce": "CRM",
    "Adobe": "ADBE", "PayPal": "PYPL", "Shopify": "SHOP", "Uber": "UBER",
    "Airbnb": "ABNB", "Johnson & Johnson": "JNJ", "Procter & Gamble": "PG",
    "Coca-Cola": "KO", "PepsiCo": "PEP", "McDonald's": "MCD", "Starbucks": "SBUX",
    "Walmart": "WMT", "Costco": "COST", "Nike": "NKE", "Disney": "DIS",
    "Berkshire Hathaway": "BRK-B", "JPMorgan Chase": "JPM", "Goldman Sachs": "GS",
    "Bank of America": "BAC", "Visa": "V", "Mastercard": "MA",
    "American Express": "AXP", "Ford": "F", "General Motors": "GM",
    "Boeing": "BA", "Lockheed Martin": "LMT", "3M": "MMM",
    "Johnson Controls": "JCI", "Caterpillar": "CAT", "ExxonMobil": "XOM",
    "Chevron": "CVX", "Pfizer": "PFE", "Moderna": "MRNA", "Gilead Sciences": "GILD"
}

# List of supported currencies
currencies = ["USD", "INR", "EUR", "GBP", "CAD", "JPY", "AUD", "CNY", "SGD"]

# Function to fetch exchange rates
def fetch_exchange_rate(target_currency, base_currency="USD"):
    url = f"https://open.er-api.com/v6/latest/{base_currency}"
    response = requests.get(url)

    print(f"\n🔍 Debug: API Response Code -> {response.status_code}")
    print(f"🔍 Debug: API Response Text -> {response.text}")

    if response.status_code == 200:
        try:
            data = response.json()
            if data.get("result") == "success":
                return data["rates"].get(target_currency)
            else:
                print(f"❌ API Error: {data.get('error-type', 'Unknown Error')}")
        except Exception as e:
            print(f"❌ JSON Parsing Error: {e}")
    else:
        print(f"❌ HTTP Error: {response.status_code}")

    return None

## calculate RSI function -> ( Relative Strength Index )
def calculate_rsi(data, window=14):
    delta = data['Close'].diff(1)
    gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    return rsi



## MACD calculation -> ( Moving Average Convergence Divergence )
def calculate_macd(data):
    short_ema = data['Close'].ewm(span=12, adjust=False).mean()
    long_ema = data['Close'].ewm(span=26, adjust=False).mean()
    macd_line = short_ema - long_ema
    signal_line = macd_line.ewm(span=9, adjust=False).mean()
    return macd_line, signal_line


# Display options
print("\n🔹 Select an option:")
print("1️⃣ Stock Price with Moving Averages")
print("2️⃣ Daily Returns Visualization with Volatility Check")
print("3️⃣ RSI Analysis")
print("4️⃣ MACD Analysis")


# Get user choice
choice = input("\nEnter your choice (1, 2, 3, or 4): ").strip()

# Validate choice
if choice not in ["1", "2", "3", "4"]:
    print("\n❌ Invalid choice! Please enter 1, 2, 3 or 4.")
    exit()

# Display available stocks
print("\n📌 Available Stocks:")
for index, (company, symbol) in enumerate(stock_symbols.items(), start=1):
    print(f"{index}. {company}: {symbol}")

# Get stock selection
company_name = input("\nEnter the company name (e.g., 'Apple', 'Tesla'): ").strip()
ticker = stock_symbols.get(company_name)

if not ticker:
    print("\n❌ Invalid company name! Please enter a valid name from the list.")
    exit()

# Fetch stock data
print(f"\n✅ Fetching stock data for {company_name} ({ticker})...")
stock_data = yf.download(ticker, period="5y")
stock_data.ffill(inplace=True)


# Currency selection
print("\n🌍 Available Currencies:", ", ".join(currencies))
base_currency = "USD"
target_currency = input("Enter target currency (e.g., 'INR', 'EUR'): ").upper()

if target_currency not in currencies:
    print("\n❌ Invalid currency!")
    exit()

# Get exchange rate
try:
    exchange_rate = c.get_rate(base_currency, target_currency)
    print(f"\n💱 Exchange Rate (1 {base_currency} = {exchange_rate} {target_currency})")
    stock_data["Close"] *= exchange_rate
except Exception as e:
    print("\n❌ Error fetching exchange rates:", e)
    exit()

# Ensure columns are in correct format
stock_data.columns = stock_data.columns.get_level_values(0)

# Fill missing values
stock_data.ffill(inplace=True)


# Function to fetch exchange rates
def fetch_exchange_rate(target_currency, base_currency="USD"):
    url = f"https://open.er-api.com/v6/latest/{base_currency}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if data.get("result") == "success":
            rates = data["rates"]
            return rates.get(target_currency)
        else:
            print(f"❌ API Error: {data.get('error-type', 'Unknown Error')}")
    else:
        print(f"❌ HTTP Error: {response.status_code}")

    return None

# Function to convert stock prices
def convert_prices(data, exchange_rate):
    if exchange_rate:
        data["Close"] = data["Close"] * exchange_rate
        return data
    else:
        print("❌ Failed to fetch exchange rate.")
        return data

# Main function to fetch and plot stock data
def fetch_and_plot_stock():
    print("\n📌 Available Stocks:")
    for company in stock_symbols.keys():
        print(f"- {company}")

    company_name = input("\nEnter the company name (e.g., 'Apple', 'Tesla'): ").strip()
    ticker = stock_symbols.get(company_name)

    if not ticker:
        print("\n❌ Invalid company name! Exiting.")
        return

    # Fetch stock data
    print(f"\n✅ Fetching stock data for {company_name} ({ticker})...")
    stock_data = yf.download(ticker, period="5y")

    # Handle missing values
    stock_data.ffill(inplace=True)

    # Get target currency
    target_currency = input("\n🌍 Enter target currency (e.g., 'INR', 'EUR'): ").strip().upper()

    # Fetch and apply exchange rate
    exchange_rate = fetch_exchange_rate(target_currency)
    if exchange_rate:
        stock_data = convert_prices(stock_data, exchange_rate)
        print(f"💱 Exchange Rate: 1 USD = {exchange_rate:.2f} {target_currency}")

    # Plot Stock Price
    plt.figure(figsize=(12, 6))
    plt.plot(stock_data["Close"], label=f"Stock Price ({target_currency})", color='blue')
    plt.title(f"{company_name} Stock Price ({target_currency})")
    plt.xlabel("Date")
    plt.ylabel(f"Price in {target_currency}")
    plt.legend()
    plt.grid(True)
    plt.show()

# ** OPTION 1: STOCK PRICE WITH MOVING AVERAGES **
if choice == "1":
    stock_data["SMA_50"] = stock_data["Close"].rolling(window=50).mean()
    stock_data["EMA_100"] = stock_data["Close"].ewm(span=100, adjust=False).mean()

    # Plot Stock Price with Moving Averages
    plt.figure(figsize=(12, 6))
    plt.plot(stock_data["Close"], label="Closing Price", color='blue', alpha=0.6)
    plt.plot(stock_data["SMA_50"], label="50-Day SMA", color='red', linestyle="dashed")
    plt.plot(stock_data["EMA_100"], label="100-Day EMA", color='green', linestyle="dashed")
    plt.title(f"{company_name} ({ticker}) Stock Price with Moving Averages")
    plt.xlabel("Date")
    plt.ylabel("Stock Price (USD)")
    plt.legend()
    plt.show()

# ** OPTION 2: DAILY RETURNS & VOLATILITY CHECK **
elif choice == "2":
    # Calculate daily returns
    stock_data["Daily Return"] = stock_data["Close"].pct_change() * 100

    # Compute standard deviation of daily returns
    volatility = stock_data["Daily Return"].std()

    # Define a threshold for high volatility (empirical value)
    VOLATILITY_THRESHOLD = 2  # Adjust as needed

    # Print volatility status
    print(f"\n📊 **Volatility Analysis for {company_name} ({ticker})**:")
    print(f"🔹 Standard Deviation of Daily Returns: {volatility:.2f}%")

    if volatility > VOLATILITY_THRESHOLD:
        print("⚠️ This is a **highly volatile** stock!")
    else:
        print("✅ This stock has **normal volatility**.")

    # Plot Daily Returns
    plt.figure(figsize=(12, 6))
    plt.plot(stock_data.index, stock_data["Daily Return"], color="purple", alpha=0.6, label="Daily Return")
    plt.axhline(y=0, color="black", linestyle="dashed", linewidth=1)
    plt.title(f"{company_name} ({ticker}) Daily Returns Over Time")
    plt.xlabel("Date")
    plt.ylabel("Daily Return (%)")
    plt.legend()
    plt.show()
elif choice == "3":
    stock_data["RSI"] = calculate_rsi(stock_data)

    # Print RSI status
    rsi_value = stock_data["RSI"].iloc[-1]
    print(f"\n📊 **RSI Analysis for {company_name} ({ticker})**:")
    print(f"🔹 Current RSI: {rsi_value:.2f}")
    if rsi_value > 70:
        print("⚠️ The stock is **overbought**. It may face a pullback.")
    elif rsi_value < 30:
        print("✅ The stock is **oversold**. It may have upside potential.")

    # Plot RSI
    plt.figure(figsize=(12, 6))
    plt.plot(stock_data["RSI"], label="RSI", color='orange')
    plt.axhline(70, linestyle='dashed', color='red', label='Overbought (70)')
    plt.axhline(30, linestyle='dashed', color='green', label='Oversold (30)')
    plt.title(f"{company_name} ({ticker}) RSI Over Time")
    plt.xlabel("Date")
    plt.ylabel("RSI")
    plt.legend()
    plt.show()
elif choice == "4":
    stock_data["MACD"], stock_data["Signal Line"] = calculate_macd(stock_data)

    # Identify Buy & Sell Signals
    stock_data['Buy_Signal'] = (stock_data['MACD'] > stock_data['Signal Line']) & \
                               (stock_data['MACD'].shift(1) <= stock_data['Signal Line'].shift(1))
    stock_data['Sell_Signal'] = (stock_data['MACD'] < stock_data['Signal Line']) & \
                                (stock_data['MACD'].shift(1) >= stock_data['Signal Line'].shift(1))

    # Print MACD status
    print(f"\n📊 **MACD Analysis for {company_name} ({ticker})**:")
    print(f"🔹 Latest MACD Value: {stock_data['MACD'].iloc[-1]:.2f}")
    print(f"🔹 Latest Signal Line Value: {stock_data['Signal Line'].iloc[-1]:.2f}")
    stock_data["MACD_Histogram"] = stock_data["MACD"] - stock_data["Signal Line"]

    if stock_data["MACD"].iloc[-1] > stock_data["Signal Line"].iloc[-1]:
        print("✅ Bullish Signal! MACD is above the Signal Line. (Price might go up)")
    else:
        print("⚠️ Bearish Signal! MACD is below the Signal Line. (Price might go down")

    # Plot MACD and Signal Line
    plt.figure(figsize=(12, 6))
    plt.bar(stock_data.index, stock_data["MACD_Histogram"], color=np.where(stock_data["MACD_Histogram"] > 0, 'green', 'red'), alpha=0.5, width=1.5, label="Histogram")
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.xticks(rotation=45)
    plt.plot(stock_data["MACD"], label="MACD Line", color='blue')
    plt.plot(stock_data["Signal Line"], label="Signal Line", color='red', linestyle="dashed")
    # Plot Buy signals (Green Dots)
    plt.scatter(stock_data.index[stock_data['Buy_Signal']],
                stock_data["MACD"][stock_data['Buy_Signal']],
                color='green', label='Buy Signal', marker='^', alpha=1)

    # Plot Sell signals (Red Dots)
    plt.scatter(stock_data.index[stock_data['Sell_Signal']],
                stock_data["MACD"][stock_data['Sell_Signal']],
                color='red', label='Sell Signal', marker='v', alpha=1)
    plt.axhline(0, linestyle='dashed', color='black', linewidth=1)
    plt.title(f"{company_name} ({ticker}) MACD Over Time")
    plt.xlabel("Date")
    plt.ylabel("MACD Value")
    plt.legend()
    plt.show()
elif choice == "5":
  fetch_and_plot_stock()
