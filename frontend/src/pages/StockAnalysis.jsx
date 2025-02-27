import { useLocation } from "react-router-dom";
import { useEffect, useState } from "react";
import { getStockPrice } from "../api/stockApi"; // API function to get current price

const StockAnalysis = () => {
  const location = useLocation();
  const { symbol, predicted_price } = location.state || {};

  const [currentPrice, setCurrentPrice] = useState(null);
  const [recommendation, setRecommendation] = useState("");

  useEffect(() => {
    const fetchCurrentPrice = async () => {
      if (!symbol) return;

      try {
        const priceData = await getStockPrice(symbol); // Get current stock price
        setCurrentPrice(priceData.current_price);

        // Determine Buy/Sell/Hold Recommendation
        if (predicted_price > priceData.current_price * 1.02) {
          setRecommendation("BUY ✅ - Expected to rise");
        } else if (predicted_price < priceData.current_price * 0.98) {
          setRecommendation("SELL ❌ - Expected to fall");
        } else {
          setRecommendation("HOLD ⏳ - Small price change expected");
        }
      } catch (error) {
        console.error("Error fetching stock price:", error);
        setRecommendation("Could not determine recommendation");
      }
    };

    fetchCurrentPrice();
  }, [symbol, predicted_price]);

  return (
    <div
      className="bg-gray-800 text-white p-10 mt-14 rounded-lg shadow-lg"
      style={{ height: "calc(100vh - 60px)" }} // Adjusting height to take up the remaining space after navbar
    >
      <h1 className="text-4xl font-bold text-center mb-6 text-blue-500">Stock Prediction</h1>
      <p className="text-center text-lg mb-4 text-gray-300">Predicted price based on historical trends</p>

      {symbol ? (
        <div className="bg-gray-700 p-8 rounded-md shadow-xl max-w-3xl mx-auto">
          <h2 className="text-2xl font-semibold text-center mb-4">Prediction Result</h2>
          <div className="space-y-4">
            <p className="text-lg font-medium"><strong>Stock:</strong> {symbol}</p>
            <p className="text-lg font-medium">
              <strong>Current Price:</strong> {currentPrice ? `$${currentPrice.toFixed(2)}` : "Loading..."} {/* Rounded to 2 digits */}
            </p>
            <p className="text-lg font-medium"><strong>Predicted Price:</strong> ${predicted_price.toFixed(2)}</p>
            <p className="text-lg font-medium">
              <strong>Recommendation:</strong>
              <span
                className={`ml-2 text-xl font-semibold 
                  ${recommendation.includes("BUY") ? "text-green-400" : 
                    recommendation.includes("SELL") ? "text-red-400" : "text-yellow-400"}`}
              >
                {recommendation}
              </span>
            </p>
          </div>
        </div>
      ) : (
        <p className="text-red-500 text-center mt-5">No prediction data available.</p>
      )}
    </div>
  );
};

export default StockAnalysis;
