import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import { useState } from "react";
import Dashboard from "./components/dashboard/Dashboard";
import StockSearch from "./components/StockSearch";
import Navbar from "./components/Navbar";
import StockAnalysis from "./pages/StockAnalysis";
import Settings from "./pages/Settings";
import Sidebar from "./components/Sidebar";
import CurrencyConverter from "./components/CurrencyConverter";
import StockMarketNews from "./components/StockMarketNews";

function App() {
  const [navbarVisible, setNavbarVisible] = useState(true);
  const [isSidebarOpen, setIsSidebarOpen] = useState(true);

  return (
    <Router>
      <Navbar setNavbarVisible={setNavbarVisible} />
      <Sidebar
        navbarVisible={navbarVisible}
        isSidebarOpen={isSidebarOpen}
        setIsSidebarOpen={setIsSidebarOpen}
      />
      <div className={`transition-all duration-300 ${
        isSidebarOpen ? "ml-64" : "ml-16"
      }`}>
        <Routes>
          <Route path="/" element={<StockSearch />} />
          <Route path="/dashboard" element={<Dashboard isSidebarOpen={isSidebarOpen} />} />
          <Route path="/currency-exchange" element={<CurrencyConverter />} />
          <Route path="/stock-analysis" element={<StockAnalysis />} />
          <Route path="/settings" element={<Settings />} />
          <Route path="/stock-news" element={<StockMarketNews />} />

        </Routes>
      </div>
    </Router>
  );
}

export default App;

