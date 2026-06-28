import { FaRobot, FaUser } from "react-icons/fa";
import "../styles/message.css";

function Message({ sender, text, time }) {
  return (
    <div className={`message ${sender}`}>
      <div className="message-avatar">
        {sender === "bot" ? <FaRobot /> : <FaUser />}
      </div>

      <div className="message-content">
        <div className="message-text">
          {text}
        </div>

        <div className="message-time">
          {time}
        </div>
      </div>
    </div>
  );
}

export default Message;