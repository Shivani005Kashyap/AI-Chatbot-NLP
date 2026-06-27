import { useState } from "react";
import API from "./services/api";
import "./styles/global.css";
import "./styles/app.css";

import ChatHeader from "./components/ChatHeader";
import MessageList from "./components/MessageList";
import ChatInput from "./components/ChatInput";


function App() {
  const [messages, setMessages] = useState([
    {
      sender: "bot",
      text: "Hello 👋 I'm your AI assistant. Ask me anything!",
    },
  ]);

  const sendMessage = async (text) => {
    const userMessage = {
      sender: "user",
      text,
    };

    setMessages((prev) => [...prev, userMessage]);

    try {
      const res = await API.post("/chat", {
        message: text,
      });

      const botMessage = {
        sender: "bot",
        text: res.data.response,
      };

      setMessages((prev) => [...prev, botMessage]);
    } catch {
      setMessages((prev) => [
        ...prev,
        {
          sender: "bot",
          text: "Unable to connect to server.",
        },
      ]);
    }
  };

  return (
    <div className="app">
      <div className="chat-container">
        <ChatHeader />
        <MessageList messages={messages} />
        <ChatInput onSend={sendMessage} />
      </div>
    </div>
  );
}

export default App;