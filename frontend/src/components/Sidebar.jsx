import { useState } from "react";
import { Link } from "react-router-dom";
import {
  FiChevronLeft,
  FiChevronRight,
  FiHome,
  FiBarChart,
  FiDatabase,
  FiSettings,
  FiGlobe,
  FiTrendingUp 
} from "react-icons/fi";
import { MdCurrencyExchange } from "react-icons/md";

const Sidebar = ({ navbarVisible, isSidebarOpen, setIsSidebarOpen }) => {
  const toggleSidebar = () => {
    setIsSidebarOpen(!isSidebarOpen);
  };

  return (
    <>
      <div
        className={`fixed left-0 ${
          navbarVisible ? "top-14" : "top-0"
        } bottom-0 bg-gray-900 text-white transition-all duration-300 z-40 border-r-white ${
          isSidebarOpen ? "w-64" : "w-16"
        }`}
      >
        <ul className="space-y-4 p-5">
          <li>
            <Link
              to="/"
              className="flex items-center space-x-2 hover:text-blue-400"
            >
              <FiHome size={24} />
              {isSidebarOpen && <span>Home</span>}
            </Link>
          </li>
          <li>
            <Link
              to="/dashboard"
              className="flex items-center space-x-2 hover:text-blue-400"
            >
              <FiBarChart size={24} />
              {isSidebarOpen && <span>Dashboard</span>}
            </Link>
          </li>
          <li>
            <Link
              to="/stock-analysis"
              className="flex items-center space-x-2 hover:text-blue-400"
            >
              <FiDatabase size={24} />
              {isSidebarOpen && <span>Stock Analysis</span>}
            </Link>
          </li>
          <li>
            <Link
              to="/settings"
              className="flex items-center space-x-2 hover:text-blue-400"
            >
              <FiSettings size={24} />
              {isSidebarOpen && <span>Settings</span>}
            </Link>
          </li>
          <Link
            to="/stock-prediction"
            className="flex items-center space-x-2 hover:text-blue-400"
          >
            <FiTrendingUp size={24} />
            {isSidebarOpen && <span>Stock Prediction</span>}
          </Link>
          <li>
            <Link
              to="/currency-exchange"
              className="flex items-center space-x-3 hover:text-blue-400"
            >
              <MdCurrencyExchange size={24} />{" "}
              {isSidebarOpen && <span>Currency Exchange</span>}
            </Link>
          </li>
          <li>
            <Link
              to="/stock-news"
              className="flex items-center space-x-2 hover:text-blue-400"
            >
              <FiGlobe size={24} />
              {isSidebarOpen && <span>Stock Market News</span>}
            </Link>
          </li>
        </ul>
      </div>

      {/* Collapse Button */}
      <button
        onClick={toggleSidebar}
        className={`fixed bottom-5 transition-all duration-300 transform -translate-x-1/2 bg-gray-800 text-white p-3 rounded-full shadow-lg cursor-pointer z-50 hover:bg-gray-700 ${
          isSidebarOpen ? "left-[13rem]" : "left-[2rem]"
        }`}
      >
        {isSidebarOpen ? (
          <FiChevronLeft size={24} />
        ) : (
          <FiChevronRight size={24} />
        )}
      </button>
    </>
  );
};

export default Sidebar;
