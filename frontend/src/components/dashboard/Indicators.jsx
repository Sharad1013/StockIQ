// Displays technical indicators like RSI & MACD.
import { Line } from "react-chartjs-2";
import { Chart, registerables } from "chart.js";
import { useEffect, useState } from "react";

Chart.register(...registerables);

const Indicators = () => {
    const [rsiData, setRsiData] = useState(null);
    const [macdData, setMacdData] = useState(null);

    useEffect(() => {
        // Example data (Replace with actual API data)
        const labels = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"];
        const rsiValues = [30, 40, 45, 50, 55, 60]; // Example RSI values
        const macdValues = [0.5, 1.0, 0.8, 1.2, 1.5, 1.8]; // Example MACD values

        setRsiData({
            labels,
            datasets: [
                {
                    label: "RSI",
                    data: rsiValues,
                    borderColor: "#FF5733",
                    backgroundColor: "rgba(255, 87, 51, 0.2)",
                    borderWidth: 2,
                    fill: true,
                },
            ],
        });

        setMacdData({
            labels,
            datasets: [
                {
                    label: "MACD",
                    data: macdValues,
                    borderColor: "#3498db",
                    backgroundColor: "rgba(52, 152, 219, 0.2)",
                    borderWidth: 2,
                    fill: true,
                },
            ],
        });
    }, []);

    return (
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4 p-4">
            <div className="bg-gray-800 p-4 rounded-lg shadow-md">
                <h2 className="text-lg font-semibold mb-2">RSI Over Time</h2>
                {rsiData ? <Line data={rsiData} /> : <p>Loading RSI...</p>}
            </div>

            <div className="bg-gray-800 p-4 rounded-lg shadow-md">
                <h2 className="text-lg font-semibold mb-2">MACD Over Time</h2>
                {macdData ? <Line data={macdData} /> : <p>Loading MACD...</p>}
            </div>
        </div>
    );
};

export default Indicators;
