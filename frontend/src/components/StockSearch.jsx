import { useState } from "react";
import Input from "../components/ui/Input";
import Button from "../components/ui/Button";

const StockSearch = () => {
  const [query, setQuery] = useState("");
  const [suggestions, setSuggestions] = useState([]);

  const stockList = [
    "AAPL - Apple Inc.", "MSFT - Microsoft Corp.", "AMZN - Amazon.com Inc.", 
    "TSLA - Tesla Inc.", "GOOGL - Alphabet Inc.", "META - Meta (Facebook)", 
    "NVDA - Nvidia", "NFLX - Netflix", "INTC - Intel", "AMD - AMD", 
    "QCOM - Qualcomm", "CSCO - Cisco Systems", "IBM - IBM", "ORCL - Oracle",
    "CRM - Salesforce", "ADBE - Adobe", "PYPL - PayPal", "SHOP - Shopify",
    "UBER - Uber", "ABNB - Airbnb", "JNJ - Johnson & Johnson", 
    "PG - Procter & Gamble", "KO - Coca-Cola", "PEP - PepsiCo", 
    "MCD - McDonald's", "SBUX - Starbucks", "WMT - Walmart", 
    "COST - Costco", "NKE - Nike", "DIS - Disney", "BRK-B - Berkshire Hathaway",
    "JPM - JPMorgan Chase", "GS - Goldman Sachs", "BAC - Bank of America",
    "V - Visa", "MA - Mastercard", "AXP - American Express", "F - Ford",
    "GM - General Motors", "BA - Boeing", "LMT - Lockheed Martin", "MMM - 3M",
    "JCI - Johnson Controls", "CAT - Caterpillar", "XOM - ExxonMobil",
    "CVX - Chevron", "PFE - Pfizer", "MRNA - Moderna", "GILD - Gilead Sciences"
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
  
  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-900 text-white">
      <div className="w-full max-w-md p-6 bg-gray-800 rounded-lg shadow-lg">
        <h2 className="text-2xl font-semibold text-center mb-4">
          Search & Select Stock
        </h2>
        <Input
          type="text"
          value={query}
          onChange={handleSearch}
          placeholder="Search for a stock..."
          className="w-full px-4 py-2 rounded-md bg-gray-700 text-white border border-gray-600 focus:ring focus:ring-blue-500"
        />
        {suggestions.length > 0 && (
          <ul className="mt-2 bg-gray-700 rounded-lg shadow-md">
            {suggestions.map((stock, index) => (
              <li
                key={index}
                className="flex justify-between items-center p-2 border-b border-gray-600 last:border-0 hover:bg-gray-600 cursor-pointer"
              >
                <span>{stock}</span>
                <Button className="bg-blue-500 hover:bg-blue-600 px-3 py-1 text-sm">
                  Select
                </Button>
              </li>
            ))}
          </ul>
        )}
      </div>
    </div>
  );
};

export default StockSearch;
