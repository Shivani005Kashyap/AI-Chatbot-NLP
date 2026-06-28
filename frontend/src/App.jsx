import { useEffect, useState } from "react";
import API from "./services/api";

import "./styles/global.css";
import "./styles/app.css";

import ChatHeader from "./components/ChatHeader";
import MessageList from "./components/MessageList";
import ChatInput from "./components/ChatInput";
import TypingIndicator from "./components/TypingIndicator";

function App() {
  const [messages, setMessages] = useState(() => {
    const saved = localStorage.getItem("chat-history");

    return saved
      ? JSON.parse(saved)
      : [
          {
            sender: "bot",
            text: "Hello 👋 I'm your AI assistant. How can I help you today?",
            time: new Date().toLocaleTimeString([], {
              hour: "2-digit",
              minute: "2-digit",
            }),
          },
        ];
  });

  const [loading, setLoading] = useState(false);

  useEffect(() => {
    localStorage.setItem("chat-history", JSON.stringify(messages));
  }, [messages]);

  const sendMessage = async (text) => {
    if (!text.trim()) return;

    const userMessage = {
      sender: "user",
      text,
      time: new Date().toLocaleTimeString([], {
        hour: "2-digit",
        minute: "2-digit",
      }),
    };

    setMessages((prev) => [...prev, userMessage]);

    setLoading(true);

    try {
      const res = await API.post("/chat", {
        message: text,
      });

      const botMessage = {
        sender: "bot",
        text: res.data.response,
        time: new Date().toLocaleTimeString([], {
          hour: "2-digit",
          minute: "2-digit",
        }),
      };

      setMessages((prev) => [...prev, botMessage]);
    } catch (error) {
      setMessages((prev) => [
        ...prev,
        {
          sender: "bot",
          text: "⚠️ Unable to connect to the server.",
          time: new Date().toLocaleTimeString([], {
            hour: "2-digit",
            minute: "2-digit",
          }),
        },
      ]);
    } finally {
      setLoading(false);
    }
  };

  const clearChat = () => {
    const firstMessage = {
      sender: "bot",
      text: "Hello 👋 I'm your AI assistant. How can I help you today?",
      time: new Date().toLocaleTimeString([], {
        hour: "2-digit",
        minute: "2-digit",
      }),
    };

    setMessages([firstMessage]);
  };

  return (
    <div className="app">
      <div className="chat-container">
        <ChatHeader onClear={clearChat} />

        <MessageList messages={messages} />

        {loading && <TypingIndicator />}

        <ChatInput onSend={sendMessage} />
      </div>
    </div>
  );
}

export default App;