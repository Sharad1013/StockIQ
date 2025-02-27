from models.stock_prediction import StockPredictor

# Initialize predictor for a stock (e.g., AAPL)
predictor = StockPredictor("AAPL")

# Train model
predictor.train_model()

# Predict the next day's price
predicted_price = predictor.predict_next_day()

print(f"Predicted Price for Next Day: {float(predicted_price):.2f}" if predicted_price is not None else "Prediction failed!")

