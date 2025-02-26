// The main dashboard layout.
import StockChart from "../StockChart";
import RSIChart from "../RSIChart";
import MACDChart from "../MACDChart";

const DashboardPage = () => {
  return (
    <div className="ml-64 p-10 text-white">
      <h1 className="text-3xl font-bold">Stock Dashboard</h1>
      <StockChart />
      <RSIChart />
      <MACDChart />
    </div>
  );
};

export default DashboardPage;
