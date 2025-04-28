import React, { useState } from 'react';
import ChatBox from './components/ChatBox';
import './styles/App.css';

function App() {
  return (
    <div className="app-container">
      <h1>FURIA Chatbot</h1>
      <ChatBox />
    </div>
  );
}

export default App;