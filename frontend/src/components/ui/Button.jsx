const Button = ({ label, onClick, className }) => {
    return (
        <button
            onClick={onClick}
            className={`px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 ${className}`}
        >
            {label}
        </button>
    );
};

export default Button;
