import { FaRobot } from "react-icons/fa";
import "./../styles/header.css";

function ChatHeader() {
  return (
    <header className="chat-header">
      <div className="header-left">
        <div className="robot-icon">
          <FaRobot />
        </div>

        <div>
          <h2>AI Chatbot</h2>
          <p>Online</p>
        </div>
      </div>

      <div className="status-dot"></div>
    </header>
  );
}

export default ChatHeader;