import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Dictionary of common stock symbols
stock_symbols = {
    "Apple": "AAPL",
    "Microsoft": "MSFT",
    "Amazon": "AMZN",
    "Tesla": "TSLA",
    "Google (Alphabet)": "GOOGL",
    "Meta (Facebook)": "META",
    "Nvidia": "NVDA",
    "Netflix": "NFLX",
    "Intel": "INTC",
    "AMD": "AMD",
    "Qualcomm": "QCOM",
    "Cisco Systems": "CSCO",
    "IBM": "IBM",
    "Oracle": "ORCL",
    "Salesforce": "CRM",
    "Adobe": "ADBE",
    "PayPal": "PYPL",
    "Shopify": "SHOP",
    "Uber": "UBER",
    "Airbnb": "ABNB",
    "Johnson & Johnson": "JNJ",
    "Procter & Gamble": "PG",
    "Coca-Cola": "KO",
    "PepsiCo": "PEP",
    "McDonald's": "MCD",
    "Starbucks": "SBUX",
    "Walmart": "WMT",
    "Costco": "COST",
    "Nike": "NKE",
    "Disney": "DIS",
    "Berkshire Hathaway": "BRK-B",
    "JPMorgan Chase": "JPM",
    "Goldman Sachs": "GS",
    "Bank of America": "BAC",
    "Visa": "V",
    "Mastercard": "MA",
    "American Express": "AXP",
    "Tesla": "TSLA",
    "Ford": "F",
    "General Motors": "GM",
    "Boeing": "BA",
    "Lockheed Martin": "LMT",
    "3M": "MMM",
    "Johnson Controls": "JCI",
    "Caterpillar": "CAT",
    "ExxonMobil": "XOM",
    "Chevron": "CVX",
    "Pfizer": "PFE",
    "Moderna": "MRNA",
    "Gilead Sciences": "GILD"
}


# Display available stocks
print("\n📌 Available Stocks:")
count = 1
for company, symbol in stock_symbols.items():
    print(f"{count}. {company}: {symbol}")
    count += 1

# Prompt user to enter a company name
company_name = input("\nEnter the company name (e.g., 'Apple', 'Tesla'): ").strip()

# Validate input and get stock symbol
ticker = stock_symbols.get(company_name)
if not ticker:
    print("\n❌ Invalid company name! Please enter a valid name from the list.")
else:
    print(f"\n✅ Fetching stock data for {company_name} ({ticker})...")

    # Fetch historical data (Last 5 years)
    stock_data = yf.download(ticker, period="5y")

    # Fix multi-index column names
    stock_data.columns = stock_data.columns.get_level_values(0)

    # Display first few rows
    print("\n📊 First 5 Rows of Stock Data:\n", stock_data.head())

    # Save data to CSV
    stock_data.to_csv(f"{ticker}_stock_data.csv")
    print(f"\n✅ Stock data saved successfully as {ticker}_stock_data.csv!")

    # Check for missing values and fill them if needed
    stock_data.ffill(inplace=True)

    # Calculate Moving Averages
    stock_data["SMA_50"] = stock_data["Close"].rolling(window=50).mean()
    stock_data["EMA_100"] = stock_data["Close"].ewm(span=100, adjust=False).mean()

    # Display first few rows with new features
    print("\n📊 Stock Data with Moving Averages:\n", stock_data[["Close", "SMA_50", "EMA_100"]].head(10))

    # 📈 Visualizing Stock Price Trends
    plt.figure(figsize=(12, 6))
    plt.plot(stock_data["Close"], label="Closing Price", color='blue', alpha=0.6)
    plt.plot(stock_data["SMA_50"], label="50-Day SMA", color='red', linestyle="dashed")
    plt.plot(stock_data["EMA_100"], label="100-Day EMA", color='green', linestyle="dashed")
    plt.title(f"{company_name} ({ticker}) Stock Price with Moving Averages")
    plt.xlabel("Date")
    plt.ylabel("Stock Price (USD)")
    plt.legend()
    plt.show()
