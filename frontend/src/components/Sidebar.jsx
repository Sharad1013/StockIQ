import { useState } from "react";
import { Link } from "react-router-dom";
import {
  FiChevronLeft,
  FiChevronRight,
  FiHome,
  FiBarChart,
  FiDatabase,
  FiSettings,
} from "react-icons/fi";

const Sidebar = () => {
  const [isOpen, setIsOpen] = useState(true);

  return (
    <>
      {/* Sidebar */}
      <div
  className={`fixed left-0 top-14 bottom-0 bg-gray-900 text-white p-5 transition-all duration-300 ${
    isOpen ? "w-66" : "w-16"
  }`}
>
        <ul className="space-y-4">
          <li>
            <Link
              to="/"
              className="flex items-center space-x-2 hover:text-blue-400"
            >
              <FiHome size={24} />
              {isOpen && <span>Home</span>}
            </Link>
          </li>
          <li>
            <Link
              to="/dashboard"
              className="flex items-center space-x-2 hover:text-blue-400"
            >
              <FiBarChart size={24} />
              {isOpen && <span>Dashboard</span>}
            </Link>
          </li>
          <li>
            <Link
              to="/stock-analysis"
              className="flex items-center space-x-2 hover:text-blue-400"
            >
              <FiDatabase size={24} /> {/* Changed icon */}
              {isOpen && <span>Stock Analysis</span>}
            </Link>
          </li>
          <li>
            <Link
              to="/settings"
              className="flex items-center space-x-2 hover:text-blue-400"
            >
              <FiSettings size={24} />
              {isOpen && <span>Settings</span>}
            </Link>
          </li>
        </ul>
      </div>

      <button
        onClick={() => setIsOpen(!isOpen)}
        className={`fixed bottom-5 transition-all duration-300 transform -translate-x-1/2 bg-gray-800 text-white p-3 rounded-full shadow-lg cursor-pointer ${
          isOpen ? "left-[14rem] " : "left-[2rem]"
        }`}
      >
        {isOpen ? <FiChevronLeft size={24} /> : <FiChevronRight size={24} />}
      </button>
    </>
  );
};

export default Sidebar;
