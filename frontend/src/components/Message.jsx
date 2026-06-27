import { FaRobot, FaUser } from "react-icons/fa";
import "../styles/message.css";

function Message({ sender, text }) {
  return (
    <div className={`message ${sender}`}>
      <div className="message-avatar">
        {sender === "bot" ? <FaRobot /> : <FaUser />}
      </div>

      <div className="message-content">
        <div className="message-text">
          {text}
        </div>
      </div>
    </div>
  );
}

export default Message;