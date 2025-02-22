import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt 

# Define stock ticker
ticker = "AAPL"  # Apple Inc.

# Fetch historical data (Last 5 years)
stock_data = yf.download(ticker, period="5y") # fetches historical data upto 5 years

# Display first few rows
print(stock_data.head())

# Save the data to a CSV file
stock_data.to_csv("AAPL_stock_data.csv")

print("Stock data saved successfully!")


# Explore the dataset 

# Check column names and data types
print(stock_data.info())

# Check for missing values
print(stock_data.isnull().sum())

# Visualise stock price trends
plt.figure(figsize=(12,6))  # Set figure size
plt.plot(stock_data["Close"], label="Closing Price", color='blue')  # Plot closing prices
plt.title("Stock Price of Apple (AAPL) Over Time")  # Set title
plt.xlabel("Date")  # Label X-axis
plt.ylabel("Stock Price (USD)")  # Label Y-axis
plt.legend()  # Show legend
plt.show()  # Display the plot

