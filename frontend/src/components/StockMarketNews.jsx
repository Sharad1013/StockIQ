import { useState, useEffect } from "react";
import { FiChevronLeft, FiChevronRight, FiSearch } from "react-icons/fi";

const StockMarketNews = () => {
  const [news, setNews] = useState([]);
  const [searchTerm, setSearchTerm] = useState("");
  const [query, setQuery] = useState("stock market");
  const [suggestions, setSuggestions] = useState([]);
  const [currentPage, setCurrentPage] = useState(1);
  const articlesPerPage = 12;
  const API_KEY = import.meta.env.VITE_NEWS_API_KEY;

  // Fetch News when query changes
  useEffect(() => {
    const fetchNews = async () => {
      try {
        const response = await fetch(
          `https://newsapi.org/v2/everything?q=${query}&apiKey=${API_KEY}`
        );
        const data = await response.json();
        if (data.articles) {
          setNews(data.articles);
          setCurrentPage(1);
        } else {
          setNews([]);
        }
      } catch (error) {
        console.error("Error fetching news:", error);
      }
    };

    fetchNews();
  }, [query]); // Runs whenever query changes

  // Generate Suggestions Dynamically
  useEffect(() => {
    if (searchTerm.length > 1) {
      setSuggestions([
        `${searchTerm} trends`,
        `${searchTerm} analysis`,
        `${searchTerm} latest news`,
        `Impact of ${searchTerm} on markets`,
        `Top companies in ${searchTerm}`,
      ]);
    } else {
      setSuggestions([]);
    }
  }, [searchTerm]);

  // Handle Search Submission
  const handleSearch = (query) => {
    if (!query.trim()) return; // Prevent empty search
    setQuery(query);
    setSearchTerm("");
    setSuggestions([]);
  };

  // Handle Enter Key Press
  const handleKeyPress = (e) => {
    if (e.key === "Enter") {
      handleSearch(searchTerm);
    }
  };

  // Pagination
  const indexOfLastArticle = currentPage * articlesPerPage;
  const indexOfFirstArticle = indexOfLastArticle - articlesPerPage;
  const currentArticles = news.slice(indexOfFirstArticle, indexOfLastArticle);

  return (
    <div className="min-h-screen bg-gray-900 text-white p-6 mt-14">
      {/* Title */}
      <h1 className="text-4xl font-bold text-blue-400">Stock Market News</h1>
      <p className="text-gray-400">Stay updated with the latest market trends</p>

      {/* Search Bar */}
      <div className="relative mt-6 w-full md:w-2/3 lg:w-1/2">
        <div className="flex items-center bg-gray-800 p-3 rounded-lg">
          <FiSearch className="text-gray-400" />
          <input
            type="text"
            placeholder="Search for news..."
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
            onKeyPress={handleKeyPress}
            className="bg-transparent outline-none w-full ml-3 text-white"
          />
        </div>

        {/* Suggestions */}
        {suggestions.length > 0 && (
          <ul className="absolute w-full bg-gray-800 mt-1 rounded-lg shadow-lg overflow-hidden z-10">
            {suggestions.map((suggestion, index) => (
              <li
                key={index}
                className="p-3 cursor-pointer hover:bg-gray-700"
                onClick={() => handleSearch(suggestion)}
              >
                {suggestion}
              </li>
            ))}
          </ul>
        )}
      </div>

      {/* News Grid */}
      <div className="mt-6 grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {currentArticles.length > 0 ? (
          currentArticles.map((article, index) => (
            <div
              key={index}
              className="bg-gray-800 p-4 rounded-lg shadow-lg transform transition duration-300 hover:scale-105 hover:rotate-1 flex flex-col"
            >
              <img
                src={article.urlToImage}
                alt="News"
                className="w-full h-40 object-cover rounded-lg"
              />
              <h2 className="text-lg font-semibold text-blue-300 mt-4">
                {article.title}
              </h2>
              <p className="text-gray-400 text-sm mt-2 flex-grow">
                {article.description}
              </p>
              <a
                href={article.url}
                target="_blank"
                rel="noopener noreferrer"
                className="mt-auto text-blue-400 block mt-4 hover:underline transition"
              >
                Read More
              </a>
            </div>
          ))
        ) : (
          <p className="text-center text-gray-400 col-span-3">
            No news found. Try searching for another topic.
          </p>
        )}
      </div>

      {/* Pagination */}
      {currentArticles.length > 0 && (
        <div className="mt-6 flex justify-center space-x-4">
          <button
            onClick={() => setCurrentPage(currentPage - 1)}
            disabled={currentPage === 1}
            className={`px-4 py-2 rounded-lg cursor-pointer flex items-center ${
              currentPage === 1
                ? "bg-gray-700 cursor-not-allowed"
                : "bg-blue-500 hover:bg-blue-600"
            }`}
          >
            <FiChevronLeft className="mr-2" />
            Prev
          </button>

          <span className="text-blue-400 text-lg">Page {currentPage}</span>

          <button
            onClick={() => setCurrentPage(currentPage + 1)}
            disabled={indexOfLastArticle >= news.length}
            className={`px-4 py-2 rounded-lg cursor-pointer flex items-center ${
              indexOfLastArticle >= news.length
                ? "bg-gray-700 cursor-not-allowed"
                : "bg-blue-500 hover:bg-blue-600"
            }`}
          >
            Next
            <FiChevronRight className="ml-2" />
          </button>
        </div>
      )}
    </div>
  );
};

export default StockMarketNews;
