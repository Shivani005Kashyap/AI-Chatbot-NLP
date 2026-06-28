import { FaRobot, FaTrash } from "react-icons/fa";
import "../styles/header.css";

function ChatHeader({ onClear }) {
  return (
    <header className="chat-header">
      <div className="header-left">
        <div className="robot-icon">
          <FaRobot />
        </div>

        <div className="header-info">
          <h2>AI Chatbot</h2>
          <p>🟢 Online</p>
        </div>
      </div>

      <button
        className="clear-btn"
        onClick={onClear}
        title="Clear Chat"
      >
        <FaTrash />
      </button>
    </header>
  );
}

export default ChatHeader;