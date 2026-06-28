import { useEffect, useRef } from "react";
import Message from "./Message";

function MessageList({ messages }) {
  const bottomRef = useRef(null);

  useEffect(() => {
    bottomRef.current?.scrollIntoView({
      behavior: "smooth",
    });
  }, [messages]);

  return (
    <div className="message-list">
      {messages.map((msg, index) => (
        <Message
          key={index}
          sender={msg.sender}
          text={msg.text}
          time={msg.time}
        />
      ))}

      <div ref={bottomRef}></div>
    </div>
  );
}

export default MessageList;