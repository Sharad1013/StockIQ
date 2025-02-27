// const BASE_URL = "http://127.0.0.1:5000"; // Your Flask backend URL

// export const predictStock = async (symbol) => {
//   try {
//     const response = await fetch(`${BASE_URL}/predict-stock?symbol=${symbol}`);
    
//     if (!response.ok) {
//       throw new Error("Failed to fetch stock prediction");
//     }
    
//     const data = await response.json();
//     return data;
//   } catch (error) {
//     console.error("Error fetching stock prediction:", error);
//     return null; // Return null to handle errors in the frontend
//   }
// };

// export const getStockPrice = async (symbol) => {
//   try {
//     const data = await yahooFinance.quote({ symbol, modules: ['price'] });
//     const currentPrice = data.price.regularMarketPrice;
//     return { current_price: currentPrice };
//   } catch (error) {
//     console.error("Error fetching stock price:", error);
//     throw error;
//   }
// };
const BASE_URL = "http://127.0.0.1:5000"; // Your Flask backend URL

export const predictStock = async (symbol) => {
  try {
    const response = await fetch(`${BASE_URL}/predict-stock?symbol=${symbol}`);
    
    if (!response.ok) {
      throw new Error("Failed to fetch stock prediction");
    }
    
    const data = await response.json();
    return data;
  } catch (error) {
    console.error("Error fetching stock prediction:", error);
    return null; // Return null to handle errors in the frontend
  }
};

// Replace the code that uses `yahoo-fin` with a request to your Flask backend
export const getStockPrice = async (symbol) => {
  try {
    const response = await fetch(`${BASE_URL}/get-stock-price?symbol=${symbol}`);
    
    if (!response.ok) {
      throw new Error("Failed to fetch stock price");
    }
    
    const data = await response.json();
    
    if (data.current_price) {
      return { current_price: data.current_price };
    } else {
      throw new Error(data.error || "Failed to fetch stock price");
    }
  } catch (error) {
    console.error("Error fetching stock price:", error);
    throw error;
  }
};
