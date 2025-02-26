//  Handles stock price visualization.
import { Line } from "react-chartjs-2";
import { Chart, registerables } from "chart.js";
import { useEffect, useState } from "react";

Chart.register(...registerables);

const StockChart = () => {
    const [chartData, setChartData] = useState(null);

    useEffect(() => {
        // Example data (Replace with actual API data)
        const fetchData = async () => {
            const labels = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"];
            const prices = [150, 170, 160, 180, 200, 210]; // Example stock prices
            const movingAvg = [155, 165, 168, 175, 190, 205]; // Example moving average

            setChartData({
                labels,
                datasets: [
                    {
                        label: "Stock Price",
                        data: prices,
                        borderColor: "#4CAF50",
                        backgroundColor: "rgba(76, 175, 80, 0.2)",
                        borderWidth: 2,
                        fill: true,
                    },
                    {
                        label: "Moving Average",
                        data: movingAvg,
                        borderColor: "#FFC107",
                        backgroundColor: "rgba(255, 193, 7, 0.2)",
                        borderWidth: 2,
                        fill: true,
                        borderDash: [5, 5], // Dotted Line
                    },
                ],
            });
        };

        fetchData();
    }, []);

    return (
        <div className="p-4 bg-gray-800 rounded-lg shadow-md">
            <h2 className="text-lg font-semibold mb-2">Stock Price & Moving Average</h2>
            {chartData ? <Line data={chartData} /> : <p>Loading Chart...</p>}
        </div>
    );
};

export default StockChart;
