# from flask import Flask
# from flask_cors import CORS  # Import CORS
# from routes.stock_routes import stock_routes  # Ensure the import matches the actual variable name

# # Initialize Flask app
# app = Flask(__name__)

# # Enable CORS (AFTER defining `app`)
# CORS(app)  # Allows frontend to make requests to backend

# # Register the blueprint
# app.register_blueprint(stock_routes)

# if __name__ == "__main__":
#     app.run(debug=True)

# from flask import Flask, jsonify, request
# from flask_cors import CORS  # Import CORS
# import yfinance as yf
# from routes.stock_routes import stock_routes  # Ensure the import matches the actual variable name

# # Initialize Flask app
# app = Flask(__name__)

# # Enable CORS (AFTER defining `app`)
# CORS(app)  # Allows frontend to make requests to backend

# # Register the blueprint
# app.register_blueprint(stock_routes)

# # Route for getting stock price
# @app.route('/get-stock-price', methods=['GET'])
# def get_stock_price():
#     symbol = request.args.get('symbol')
#     if not symbol:
#         return jsonify({'error': 'Symbol is required'}), 400

#     try:
#         stock = yf.Ticker(symbol)
#         data = stock.history(period='1d')
#         current_price = data['Close'].iloc[-1]  # Get the last closing price
#         return jsonify({'current_price': current_price})
#     except Exception as e:
#         return jsonify({'error': str(e)}), 500

# if __name__ == "__main__":
#     app.run(debug=True)




from flask import Flask, jsonify, request
from flask_cors import CORS  # Import CORS
import yfinance as yf
from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd
from routes.stock_routes import stock_routes  # Ensure the import matches the actual variable name

# Initialize Flask app
app = Flask(__name__)

# Enable CORS (AFTER defining `app`)
CORS(app)  # Allows frontend to make requests to backend

# Register the blueprint
app.register_blueprint(stock_routes)

# Route for getting stock price
@app.route('/get-stock-price', methods=['GET'])
def get_stock_price():
    symbol = request.args.get('symbol')
    if not symbol:
        return jsonify({'error': 'Symbol is required'}), 400

    try:
        stock = yf.Ticker(symbol)
        data = stock.history(period='1d')
        current_price = data['Close'].iloc[-1]  # Get the last closing price
        return jsonify({'current_price': current_price})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route for stock price prediction using Linear Regression
@app.route('/predict-stock-price', methods=['GET'])
def predict_stock_price():
    symbol = request.args.get('symbol')
    if not symbol:
        return jsonify({'error': 'Symbol is required'}), 400

    try:
        # Fetch historical stock data
        stock = yf.Ticker(symbol)
        data = stock.history(period='1y')  # 1 year of data
        data['Date'] = data.index

        # Prepare the data for Linear Regression
        data['Date'] = pd.to_datetime(data['Date'])
        data['Date'] = data['Date'].map(lambda x: x.toordinal())  # Convert to ordinal

        # Use 'Date' as the feature and 'Close' price as the target
        X = data[['Date']]  # Features (Date)
        y = data['Close']  # Target (Close price)

        # Train a Linear Regression model
        model = LinearRegression()
        model.fit(X, y)

        # Predict the stock price for the next day (using today's date)
        prediction_date = pd.to_datetime('today').toordinal()
        predicted_price = model.predict([[prediction_date]])

        return jsonify({'predicted_price': predicted_price[0]})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    


if __name__ == "__main__":
    app.run(debug=True)
