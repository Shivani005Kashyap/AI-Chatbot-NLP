import "../styles/typing.css";

function TypingIndicator() {
  return (
    <div className="typing-container">
      <div className="typing-avatar">🤖</div>

      <div className="typing-bubble">
        <span></span>
        <span></span>
        <span></span>
      </div>
    </div>
  );
}

export default TypingIndicator;