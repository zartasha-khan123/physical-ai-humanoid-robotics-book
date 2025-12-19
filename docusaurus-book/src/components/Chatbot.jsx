// docusaurus-book/src/components/Chatbot.jsx
import React, { useState, useEffect, useRef } from 'react';
import './Chatbot.css';

// For local development, point this to your FastAPI backend.
// For production on Vercel, use relative path like '/api/query' if rewrites are set.
const API_ENDPOINT = 'http://127.0.0.1:8000/query';

export default function Chatbot() {
  const [isOpen, setIsOpen] = useState(false);
  const [messages, setMessages] = useState([]);
  const [userInput, setUserInput] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [selectedText, setSelectedText] = useState(null);
  const messagesEndRef = useRef(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };
  useEffect(scrollToBottom, [messages]);

  useEffect(() => {
    const handleTextSelection = () => {
      const selection = window.getSelection().toString().trim();
      if (selection) {
        setSelectedText(selection);
      }
    };
    document.addEventListener('mouseup', handleTextSelection);
    return () => document.removeEventListener('mouseup', handleTextSelection);
  }, []);

  const toggleChat = () => {
    setIsOpen(!isOpen);
    if (!isOpen && messages.length === 0) {
      setMessages([
        {
          sender: 'bot',
          text: 'Hello! I am your AI assistant. Ask me anything about this book or select text to ask context-specific questions.',
        },
      ]);
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!userInput.trim()) return;

    const query = userInput;
    const context = selectedText;

    setUserInput('');
    setSelectedText(null);
    setMessages((prev) => [...prev, { sender: 'user', text: query }]);
    setIsLoading(true);

    try {
      const payload = { query };
      if (context) payload.selected_text = context;

      const response = await fetch(API_ENDPOINT, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload),
      });

      if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);

      const data = await response.json();

      let botResponse = data.answer || 'Sorry, I could not find an answer.';

      // Only add Sources if metadata exists AND query is not a default greeting
if (data.metadata && data.metadata.length > 0 && query.toLowerCase() !== "hello") {
  const sources = data.metadata
    .map(meta => `- [${meta.section || 'Source'}](${meta.source_url})`)
    .join('\n');
  botResponse += `\n\n**Sources:**\n${sources}`;
}

      setMessages((prev) => [...prev, { sender: 'bot', text: botResponse }]);
    } catch (err) {
      setMessages((prev) => [
        ...prev,
        { sender: 'bot', text: 'Sorry, I encountered an error connecting to the server.' },
      ]);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="chatbot-container">
      <button
        className={`chatbot-toggle ${isOpen ? 'open' : ''}`}
        onClick={toggleChat}
        aria-label="Toggle AI Assistant"
      >
        💬
      </button>

      {isOpen && (
        <div className="chatbot-window" role="dialog" aria-modal="true">
          <div className="chatbot-header">
            <h4>AI Assistant</h4>
            <button onClick={toggleChat} aria-label="Close chat">X</button>
          </div>

          <div className="chatbot-messages">
            {messages.map((m, i) => (
              <div key={i} className={`message ${m.sender}`}>
                <div className="message-text">
                  {m.text.split('\n').map((line, idx) => (
                    <div
                      key={idx}
                      dangerouslySetInnerHTML={{ __html: line.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>') }}
                    />
                  ))}
                </div>
              </div>
            ))}
            {isLoading && <div className="message bot"><p>...</p></div>}
            <div ref={messagesEndRef} />
          </div>

          {selectedText && (
            <div className="selected-text-notice">
              <p>Context: "{selectedText.substring(0, 80)}..."</p>
              <button onClick={() => setSelectedText(null)} aria-label="Clear context">X</button>
            </div>
          )}

          <form className="chatbot-input" onSubmit={handleSubmit}>
            <input
              type="text"
              value={userInput}
              onChange={(e) => setUserInput(e.target.value)}
              placeholder="Ask a question..."
              aria-label="Chat input"
            />
            <button type="submit" aria-label="Send message">Send</button>
          </form>
        </div>
      )}
    </div>
  );
}
