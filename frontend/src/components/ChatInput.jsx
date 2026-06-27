import { useState } from "react";
import { FaPaperPlane } from "react-icons/fa";
import "../styles/input.css";

function ChatInput({ onSend }) {
  const [message, setMessage] = useState("");

  const send = () => {
    if (!message.trim()) return;

    onSend(message);
    setMessage("");
  };

  return (
    <div className="chat-input">
      <input
        type="text"
        placeholder="Ask me anything..."
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        onKeyDown={(e) => {
          if (e.key === "Enter") send();
        }}
      />

      <button onClick={send}>
        <FaPaperPlane />
      </button>
    </div>
  );
}

export default ChatInput;