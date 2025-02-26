import os
from pymongo import MongoClient
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get MongoDB URI from environment variables
mongo_uri = os.getenv("MONGO_URI")

# Establish connection
client = MongoClient(mongo_uri)
db = client["StockIQ"]
collection = db["stock_data"]

print("✅ Successfully connected to MongoDB Atlas!")

# Export the collection so other files can use it
def get_collection():
    return collection
