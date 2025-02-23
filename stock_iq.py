import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

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

# Ensure columns are in correct format
stock_data.columns = stock_data.columns.get_level_values(0)

# Fill missing values
stock_data.ffill(inplace=True)

# ** OPTION 1: STOCK PRICE WITH MOVING AVERAGES **
if choice == "1":
    stock_data["SMA_50"] = stock_data["Close"].rolling(window=50).mean()
    stock_data["EMA_100"] = stock_data["Close"].ewm(span=100, adjust=False).mean()

    # Plot Stock Price with Moving Averages
    plt.figure(figsize=(12, 6))
    plt.plot(stock_data["Close"], label="Closing Price", color='blue', alpha=0.6)
    plt.plot(stock_data["SMA_50"], label="50-Day SMA", color='red', linestyle="dashed")
    plt.plot(stock_data["EMA_100"], label="100-Day EMA", color='green', linestyle="dashed")
    plt.grid(True, linestyle="--", alpha=0.5)
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
    plt.grid(True, linestyle="--", alpha=0.5)
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
    plt.grid(True, linestyle="--", alpha=0.5)
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
