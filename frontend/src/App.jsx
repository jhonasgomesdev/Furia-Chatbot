import React, { useState, useEffect } from 'react';
import ChatBox from './components/ChatBox';
import './styles/landing.css';
import './styles/chatbox.css';

function App() {
  const [isChatOpen, setIsChatOpen] = useState(false);
  const [showTooltip, setShowTooltip] = useState(true);

  useEffect(() => {
    const timer = setTimeout(() => {
      setShowTooltip(false);
    }, 5000); // Tooltip desaparece após 5 segundos

    return () => clearTimeout(timer);
  }, []);

  return (
    <div className="landing-container">
      {/* Header */}
      <header className="landing-header">
        <div className="logo-area">
          <img src="/logo-furia.png" alt="FURIA Logo" className="furia-logo" />
        </div>
        <div className="nav-buttons">
          <a href="https://furia.gg/">
            <button className="nav-btn">Store</button>
          </a>
          <a href="https://x.com/FURIA">
            <button className="nav-btn">Notices by X</button>
          </a>
          <a href="https://www.instagram.com/furiagg/">
            <button className="nav-btn">Instagram</button>
          </a>
        </div>
      </header>

      {/* Main Content */}
      <main className="landing-main">
        <a href="https://furia.gg/" target="_blank" rel="noopener noreferrer" className="fullbanner-link">
          <img src="/adidas-furia.png" alt="Furia Store" className="fullbanner-image"/>
        </a> 
        <h1 className="hero-title">ENTRE NO UNIVERSO DA FURIA</h1>
        <p className="hero-subtitle">E fale com a <strong>Pantera</strong>, nossa assistente virtual oficial!</p>
        <div className="furia-video-container">
          <video src="/furia-gif.mp4" autoPlay loop muted playsInline className="furia-video"/>
        </div>
      </main>

      {/* Chat Toggle Button com Tooltip */}
      <div className="chat-toggle-wrapper">
        {showTooltip && <div className="chat-tooltip">Fale com a Pantera</div>}
        <button
          className="chat-toggle-button"
          onClick={() => setIsChatOpen(prev => !prev)}
          aria-label="Abrir chat"
        >
          <img src="/bot.png" alt="Abrir chat" className="chat-icon" />
        </button>
      </div>

      {/* ChatBox */}
      {isChatOpen && (
        <div className="chatbox-container">
          <ChatBox />
        </div>
      )}
      
      {/* Footer */}
      <footer className="landing-footer">
        <p>FURIA Esports © {new Date().getFullYear()} – Todos os direitos reservados.</p>
      </footer>
    </div>
  );
}

export default App;
