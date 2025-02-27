import pymongo
import pandas as pd

# MongoDB Connection
client = pymongo.MongoClient("your_mongodb_connection_string")
db = client["stockiq"]  # Your database name
collection = db["historical_stock_data"]  # Your collection name

def fetch_stock_data(symbol, start_date=None, end_date=None):
    """
    Fetch historical stock data for a given symbol from MongoDB.
    Optionally filter by start_date and end_date.
    """
    query = {"symbol": symbol}
    
    # Apply date filters if provided
    if start_date and end_date:
        query["date"] = {"$gte": start_date, "$lte": end_date}

    # Fetch data from MongoDB
    stock_data = list(collection.find(query, {"_id": 0}))  # Exclude MongoDB ID
    
    # Convert to Pandas DataFrame
    df = pd.DataFrame(stock_data)
    
    # Convert 'date' column to datetime format
    df["date"] = pd.to_datetime(df["date"])
    
    # Sort by date (oldest to newest)
    df = df.sort_values(by="date")
    
    return df

# Example Usage
df = fetch_stock_data("AAPL", "2023-01-01", "2024-01-01")
print(df.head())  # Preview the data
