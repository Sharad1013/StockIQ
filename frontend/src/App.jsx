import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Dashboard from "./components/dashboard/Dashboard";
import StockSearch from "./components/StockSearch";
import Navbar from "./components/Navbar";
import Home from "./pages/Home";
import StockDashboard from "./pages/StockDashboard";
import StockAnalysis from "./pages/StockAnalysis";
import Settings from "./pages/Settings";
import Sidebar from "./components/Sidebar";

function App() {
  return (
    <Router>
      <Navbar />
      <Sidebar/>
      <Routes>
        <Route path="/" element={<StockSearch />} />
        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="/stock-analysis" element={<StockAnalysis />} />
        <Route path="/settings" element={<Settings />} />
      </Routes>
    </Router>
  );
}

export default App;
