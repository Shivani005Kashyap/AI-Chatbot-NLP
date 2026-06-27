import { useState } from "react";
import axios from "axios";

function App() {
  const [message, setMessage] = useState("");
  const [messages, setMessages] = useState([
    {
      sender: "bot",
      text: "Hello! 👋 How can I help you today?",
    },
  ]);

  const sendMessage = async () => {
    if (message.trim() === "") return;

    const userMessage = {
      sender: "user",
      text: message,
    };

    setMessages((prev) => [...prev, userMessage]);

    try {
      const res = await axios.post("http://127.0.0.1:5000/chat", {
        message: message,
      });

      const botMessage = {
        sender: "bot",
        text: res.data.response,
      };

      setMessages((prev) => [...prev, botMessage]);
    } catch (error) {
      setMessages((prev) => [
        ...prev,
        {
          sender: "bot",
          text: "Unable to connect to server.",
        },
      ]);
    }

    setMessage("");
  };

  return (
    <div
      style={{
        height: "100vh",
        background: "#f4f4f4",
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
      }}
    >
      <div
        style={{
          width: "420px",
          height: "650px",
          background: "white",
          borderRadius: "15px",
          display: "flex",
          flexDirection: "column",
          boxShadow: "0 0 20px rgba(0,0,0,.2)",
        }}
      >
        <div
          style={{
            background: "#4F46E5",
            color: "white",
            padding: "18px",
            textAlign: "center",
            fontSize: "22px",
            fontWeight: "bold",
          }}
        >
          🤖 AI Chatbot
        </div>

        <div
          style={{
            flex: 1,
            overflowY: "auto",
            padding: "15px",
          }}
        >
          {messages.map((msg, index) => (
            <div
              key={index}
              style={{
                textAlign: msg.sender === "user" ? "right" : "left",
                marginBottom: "12px",
              }}
            >
              <span
                style={{
                  display: "inline-block",
                  padding: "10px 14px",
                  borderRadius: "12px",
                  background:
                    msg.sender === "user" ? "#4F46E5" : "#E5E7EB",
                  color: msg.sender === "user" ? "white" : "black",
                  maxWidth: "80%",
                }}
              >
                {msg.text}
              </span>
            </div>
          ))}
        </div>

        <div
          style={{
            display: "flex",
            padding: "15px",
            borderTop: "1px solid #ddd",
          }}
        >
          <input
            type="text"
            value={message}
            placeholder="Type a message..."
            onChange={(e) => setMessage(e.target.value)}
            onKeyDown={(e) => {
              if (e.key === "Enter") sendMessage();
            }}
            style={{
              flex: 1,
              padding: "12px",
              borderRadius: "8px",
              border: "1px solid #ccc",
            }}
          />

          <button
            onClick={sendMessage}
            style={{
              marginLeft: "10px",
              padding: "12px 18px",
              background: "#4F46E5",
              color: "white",
              border: "none",
              borderRadius: "8px",
              cursor: "pointer",
            }}
          >
            Send
          </button>
        </div>
      </div>
    </div>
  );
}

export default App;