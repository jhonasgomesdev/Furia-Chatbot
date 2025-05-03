import React, { useState, useEffect, useRef } from 'react';
import axios from 'axios';

function ChatBox() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');
  const [loading, setLoading] = useState(false);
  const messagesEndRef = useRef(null);

  const sendMessage = async () => {
    if (loading || !input.trim()) return;

    const userMessage = {
      sender: 'user',
      text: input,
      time: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
    };

    const updatedMessages = [...messages, userMessage];
    setMessages(updatedMessages);
    setInput('');
    setLoading(true);

    try {
      const response = await axios.post('http://127.0.0.1:8000/chat', {
        message: input
      });

      const botMessage = {
        sender: 'bot',
        text: response.data.reply,
        time: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
      };

      setMessages([...updatedMessages, botMessage]);
    } catch (error) {
      const errorMessage = {
        sender: 'bot',
        text: 'Erro ao se conectar com o servidor.',
        time: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
      };
      setMessages([...updatedMessages, errorMessage]);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    if (messages.length === 0) {
      const loadingMessage = {
        sender: 'bot',
        text: 'Digitando...',
        time: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
      };
  
      setMessages([loadingMessage]);
  
      setTimeout(() => {
        setMessages([{
          sender: 'bot',
          text: 'Fala guerreiro! Eu sou a Pantera, o chatbot do time de CS da Fúria, como posso te ajudar?',
          time: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
        }]);
      }, 1500); // 1 segundo de delay
    }
  }, []);
  

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

  return (
    <div className="chatbox">
      <div className="messages">
        {messages.map((msg, index) => (
          <div key={index} className={`message ${msg.sender}`}>
            <div className="bubble">
              {msg.sender === 'bot' && (
                <img src="/bot.png" alt="Bot Avatar" className="avatar bot" />
              )}
              <div>
                <div className="text">
                  {msg.text}
                  <span className="time">{msg.time}</span>
                </div>
              </div>
            </div>
          </div>
        ))}

        {loading && (
          <div className="message bot">
            <div className="bubble">
              <img src="/bot.png" alt="Bot Avatar" className="avatar bot" />
              <div className="text">Digitando...</div>
            </div>
          </div>
        )}

        <div ref={messagesEndRef} />
      </div>

      <div className="input-area">
        <input
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={(e) => e.key === 'Enter' && sendMessage()}
          placeholder="Digite sua mensagem..."
        />
        <button onClick={sendMessage}>Enviar</button>
      </div>
    </div>
  );
}

export default ChatBox;
