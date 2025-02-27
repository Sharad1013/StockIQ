import { useState, useEffect } from "react";

const CurrencyConverter = () => {
  const [rates, setRates] = useState({});
  const [apiDate, setApiDate] = useState(""); // Stores the API date
  const [fromCurrency, setFromCurrency] = useState("USD");
  const [toCurrency, setToCurrency] = useState("EUR");
  const [amount, setAmount] = useState(1);
  const [convertedAmount, setConvertedAmount] = useState(null);

  // Fetch exchange rates on component mount
  useEffect(() => {
    fetch("https://api.exchangerate-api.com/v4/latest/USD")
      .then((response) => response.json())
      .then((data) => {
        setRates(data.rates);
        setApiDate(data.date); // Extracting the date from API response
      })
      .catch((error) => console.error("Error fetching exchange rates:", error));
  }, []);

  // Automatically convert whenever amount, fromCurrency, or toCurrency changes
  useEffect(() => {
    if (rates[fromCurrency] && rates[toCurrency]) {
      const result = (amount / rates[fromCurrency]) * rates[toCurrency];
      setConvertedAmount(result.toFixed(2));
    }
  }, [amount, fromCurrency, toCurrency, rates]);

  return (
    <div className="min-h-screen bg-gray-900 text-white p-6 mt-14">
      <h1 className="text-4xl font-bold text-blue-400">Currency Exchange</h1>
      <p className="text-gray-400">Check live exchange rates and convert currencies</p>

      {/* Exchange Rates Table */}
      <div className="mt-6 max-h-[400px] overflow-y-auto border border-gray-700 rounded-lg">
        <table className="w-full bg-gray-800 rounded-lg shadow-lg">
          <thead className="sticky top-0 bg-gray-700 text-blue-300">
            <tr>
              <th className="p-3 text-left">Currency</th>
              <th className="p-3 text-left">Exchange Rate (1 USD)</th>
              <th className="p-3 text-left">Last Updated</th> {/* New Column */}
            </tr>
          </thead>
          <tbody>
            {Object.entries(rates).map(([currency, rate], index) => (
              <tr
                key={currency}
                className={`border-b border-gray-700 ${
                  index % 2 === 0 ? "bg-opacity-50" : "bg-opacity-80"
                }`}
              >
                <td className="p-3">{currency}</td>
                <td className="p-3">{rate.toFixed(4)}</td>
                <td className="p-3 text-gray-400">{apiDate}</td> {/* Using API Date */}
              </tr>
            ))}
          </tbody>
        </table>
      </div>

      {/* Currency Converter */}
      <div className="mt-6 bg-gray-800 p-6 rounded-lg shadow-lg">
        <h2 className="text-xl font-semibold text-blue-300">Convert Currency</h2>
        <div className="flex flex-col md:flex-row gap-4 mt-4">
          <input
            type="number"
            className="p-3 rounded bg-gray-700 text-white w-full md:w-1/3"
            placeholder="Enter amount"
            value={amount}
            onChange={(e) => setAmount(e.target.value)}
          />
          <select
            className="p-3 rounded bg-gray-700 text-white"
            value={fromCurrency}
            onChange={(e) => setFromCurrency(e.target.value)}
          >
            {Object.keys(rates).map((currency) => (
              <option key={currency} value={currency}>
                {currency}
              </option>
            ))}
          </select>
          <select
            className="p-3 rounded bg-gray-700 text-white"
            value={toCurrency}
            onChange={(e) => setToCurrency(e.target.value)}
          >
            {Object.keys(rates).map((currency) => (
              <option key={currency} value={currency}>
                {currency}
              </option>
            ))}
          </select>
        </div>
        {convertedAmount !== null && (
          <p className="mt-4 text-lg text-blue-400">
            {amount} {fromCurrency} = {convertedAmount} {toCurrency}
          </p>
        )}
      </div>
    </div>
  );
};

export default CurrencyConverter;
