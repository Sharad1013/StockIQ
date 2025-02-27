import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { predictStock } from "../api/stockApi"; // API function
import Input from "../components/ui/Input";
import Button from "../components/ui/Button";

const StockSearch = () => {
  const [query, setQuery] = useState("");
  const [suggestions, setSuggestions] = useState([]);
  const [prediction, setPrediction] = useState(null);
  const [error, setError] = useState(null);
  const navigate = useNavigate();

  const stockList = [
    "AAPL - Apple Inc.",
    "MSFT - Microsoft Corp.",
    "AMZN - Amazon.com Inc.",
    "TSLA - Tesla Inc.",
    "GOOGL - Alphabet Inc.",
    "META - Meta (Facebook)",
    "NVDA - Nvidia",
    "NFLX - Netflix",
    "INTC - Intel",
    "AMD - AMD",
    "QCOM - Qualcomm",
    "CSCO - Cisco Systems",
    "IBM - IBM",
    "ORCL - Oracle",
    "CRM - Salesforce",
    "ADBE - Adobe",
    "PYPL - PayPal",
    "SHOP - Shopify",
    "UBER - Uber",
    "ABNB - Airbnb",
    "JNJ - Johnson & Johnson",
    "PG - Procter & Gamble",
    "KO - Coca-Cola",
    "PEP - PepsiCo",
    "MCD - McDonald's",
    "SBUX - Starbucks",
    "WMT - Walmart",
    "COST - Costco",
    "NKE - Nike",
    "DIS - Disney",
    "BRK-B - Berkshire Hathaway",
    "JPM - JPMorgan Chase",
    "GS - Goldman Sachs",
    "BAC - Bank of America",
    "V - Visa",
    "MA - Mastercard",
    "AXP - American Express",
    "F - Ford",
    "GM - General Motors",
    "BA - Boeing",
    "LMT - Lockheed Martin",
    "MMM - 3M",
    "JCI - Johnson Controls",
    "CAT - Caterpillar",
    "XOM - ExxonMobil",
    "CVX - Chevron",
    "PFE - Pfizer",
    "MRNA - Moderna",
    "GILD - Gilead Sciences",
  ];

  const handleSearch = (e) => {
    const searchTerm = e.target.value.trim().toLowerCase();
    setQuery(e.target.value);

    if (searchTerm.length > 1) {
      setSuggestions(
        stockList.filter((stock) => stock.toLowerCase().includes(searchTerm))
      );
    } else {
      setSuggestions([]);
    }
  };

  const selectStock = async (stock) => {
    setQuery(stock);
    setSuggestions([]);
  
    const symbol = stock.split(" - ")[0]; // Extract stock symbol
  
    try {
      setError(null);
      setPrediction(null);
      const result = await predictStock(symbol);
  
      if (result) {
        setPrediction(result.predicted_price);
        navigate("/stock-prediction", { 
          state: { 
            symbol: symbol, 
            predicted_price: result.predicted_price 
          }
        });
      } else {
        setError("Failed to fetch stock prediction");
      }
    } catch (err) {
      setError("An error occurred while fetching prediction");
    }
  };
  
  return (
    <div className="relative flex-grow">
      {/* Video Wrapper - Ensures it does not hide the sidebar */}
      <div className="absolute top-0 left-0 w-full h-full overflow-hidden -z-10">
        <video autoPlay loop muted className="w-full h-full object-cover">
          <source src="/media/Stock_IQ.mp4" type="video/mp4" />
          Your browser does not support the video tag.
        </video>
      </div>

      {/* Content */}
      <div className="relative flex items-center justify-center h-screen z-20">
        <div className="w-full max-w-lg p-6 bg-gray-900/90 rounded-lg shadow-xl border border-gray-700">
          <h2 className="text-2xl font-semibold text-center mb-4 text-blue-400">
            Search & Select Stock
          </h2>
          <div className="relative">
            <input
              type="text"
              value={query}
              onChange={handleSearch}
              placeholder="Search for a stock..."
              className="w-full px-4 py-3 rounded-md bg-gray-800 text-white border border-gray-600 
        focus:ring focus:ring-blue-500 focus:border-blue-500 placeholder-gray-400 shadow-md"
            />

            {/* Dropdown for search results */}
            {suggestions.length > 0 && (
              <ul
                className="absolute top-full left-0 w-full bg-gray-900 border border-gray-700 
        rounded-md shadow-lg mt-1 z-50"
              >
                {suggestions.map((result, index) => (
                  <li
                    key={index}
                    className="p-3 text-white hover:bg-blue-600 cursor-pointer transition-all"
                    onClick={() => selectStock(result)}
                  >
                    {result}
                  </li>
                ))}
              </ul>
            )}
          </div>

          {/* Show Prediction */}
          {prediction && (
            <div className="mt-4 text-center">
              <p className="text-lg text-green-400 font-semibold">
                Predicted Price: ${prediction}
              </p>
            </div>
          )}

          {/* Show Error Message */}
          {error && (
            <div className="mt-4 text-center">
              <p className="text-lg text-red-500 font-semibold">{error}</p>
            </div>
          )}
        </div>
      </div>
    </div>
  );
};

export default StockSearch;
