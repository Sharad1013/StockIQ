import { Link } from "react-router-dom";
import { FiHome, FiBarChart, FiDatabase, FiSettings } from "react-icons/fi";
import { useState, useEffect } from "react";

const Navbar = ({ setNavbarVisible }) => {
  const [isVisible, setIsVisible] = useState(true);
  let lastScrollY = window.scrollY;

  useEffect(() => {
    const handleScroll = () => {
      const scrollY = window.scrollY;
      const isScrollingDown = scrollY > lastScrollY;

      if (isScrollingDown && isVisible) {
        setIsVisible(false);
        setNavbarVisible(false);
      } else if (!isScrollingDown && !isVisible) {
        setIsVisible(true);
        setNavbarVisible(true);
      }

      lastScrollY = scrollY;
    };

    window.addEventListener("scroll", handleScroll);
    return () => window.removeEventListener("scroll", handleScroll);
  }, [isVisible, setNavbarVisible]);

  return (
    <nav
      className={`fixed top-0 w-full bg-gray-800 text-white p-4 flex space-x-4 z-50 transition-all duration-500 ${
        isVisible ? "opacity-100 translate-y-0" : "opacity-0 -translate-y-full"
      }`}
    >
      <div className="flex items-center gap-1">
        <FiHome size={24} />
        <Link to="/" className="hover:text-blue-400">Home</Link>
      </div>
      <div className="flex items-center gap-1">
        <FiBarChart size={24} />
        <Link to="/dashboard" className="hover:text-blue-400">Dashboard</Link>
      </div>
      <div className="flex items-center gap-1">
        <FiDatabase size={24} />
        <Link to="/stock-analysis" className="hover:text-blue-400">Stock Analysis</Link>
      </div>
      <div className="flex items-center gap-1">
        <FiSettings size={24} />
        <Link to="/settings" className="hover:text-blue-400">Settings</Link>
      </div>
    </nav>
  );
};

export default Navbar;

