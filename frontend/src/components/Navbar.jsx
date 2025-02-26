import { Link } from "react-router-dom";
import {
  FiChevronLeft,
  FiChevronRight,
  FiHome,
  FiBarChart,
  FiDatabase,
  FiSettings,
} from "react-icons/fi";
const Navbar = () => {
  return (
    <nav className="bg-gray-800 text-white p-4 flex space-x-4">
      <div className="flex items-center gap-1">
        <FiHome size={24} />
        <Link to="/" className="hover:text-blue-400">
          Home
        </Link>
      </div>
      <div className="flex items-center gap-1">
        <FiBarChart size={24} />
        <Link to="/dashboard" className="hover:text-blue-400">
          Dashboard
        </Link>
      </div>
      <div className="flex items-center gap-1">
        <FiDatabase size={24} />
        <Link to="/stock-analysis" className="hover:text-blue-400">
          Stock Analysis
        </Link>
      </div>
      <div className="flex items-center gap-1">
        <FiSettings size={24} />
        <Link to="/settings" className="hover:text-blue-400">
          Settings
        </Link>
      </div>
    </nav>
  );
};

export default Navbar;
