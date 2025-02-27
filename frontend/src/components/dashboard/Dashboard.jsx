// The main dashboard layout.
import StockChart from "../StockChart";
import RSIChart from "../RSIChart";
import MACDChart from "../MACDChart";
import CurrencyConverter from "../CurrencyConverter";
const Dashboard = ({ isSidebarOpen }) => {
  return (
    <div
      className={`min-h-screen bg-gray-900 text-white p-6 transition-all duration-300 mt-14 ${
        isSidebarOpen ? "ml-0" : "ml-0"
      }`}
    >
      <h1 className="text-4xl font-bold text-blue-400">Stock Dashboard</h1>
      <p className="text-gray-400">
        Analyze the latest stock trends and indicators
      </p>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-6 mt-6">
        <div className="bg-gray-800 p-4 rounded-lg shadow-lg">
          <h2 className="text-xl font-semibold text-blue-300">
            Stock Price & Moving Average
          </h2>
          <StockChart />
        </div>

        <div className="bg-gray-800 p-4 rounded-lg shadow-lg">
          <h2 className="text-xl font-semibold text-blue-300">RSI Over Time</h2>
          <RSIChart />
        </div>
      </div>

      <div className="bg-gray-800 p-4 rounded-lg shadow-lg mt-6">
        <h2 className="text-xl font-semibold text-blue-300">MACD Analysis</h2>
        <MACDChart />
      </div>
    </div>
  );
};

export default Dashboard;
