from flask import Blueprint, request, jsonify
from models.stock_prediction import StockPredictor

stock_routes = Blueprint('stock_routes', __name__)  # ✅ Ensure this is stock_routes

@stock_routes.route('/predict-stock', methods=['GET'])
def predict_stock():
    symbol = request.args.get('symbol')
    
    if not symbol:
        return jsonify({"error": "Stock symbol is required"}), 400

    try:
        predictor = StockPredictor(symbol)
        predictor.train_model()  # Ensure the model is trained before predicting
        predicted_price = predictor.predict_next_day()

        return jsonify({
            "symbol": symbol,
            "predicted_price": round(predicted_price, 2)
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500
