# 🐾 Chatbot Interativo FURIA

Este projeto é parte do desafio **"Experiência Conversacional FURIA"**, cujo objetivo é proporcionar uma experiência única de conversa para fãs da equipe FURIA de CS:GO. A plataforma conta com uma **interface amigável em React**, um **backend inteligente em FastAPI com scraping da Liquipedia** e respostas traduzidas com estilo usando a **Gemini API**.

---

## 🧩 Tecnologias Utilizadas

### Frontend
- React + Vite
- CSS customizado
- localStorage
- Fetch API

### Backend
- FastAPI
- Python 3.10+
- Selenium + BeautifulSoup
- Gemini API (Google Generative AI)

---

## ✨ Funcionalidades

- 💬 Chatbot que responde perguntas sobre jogadores, técnico e últimas partidas da FURIA.
- 🔍 Scraping em tempo real da [Liquipedia - FURIA](https://liquipedia.net/counterstrike/FURIA).
- 🌍 Tradução estilizada e empolgada com Gemini API.
- 🧠 Histórico de conversa salvo no navegador.
- 🛒 Landing page:
  - Banner redireciona para [FURIA.gg](https://www.furia.gg/)
  - Vídeo institucional em looping.

---

## 📁 Estrutura do Projeto
```text
📦 chatbot-furia/
├── backend/
│   ├── main.py             # API com FastAPI
│   ├── liquipedia.py       # Scraping da Liquipedia
│   ├── responses.py        # Integração com Gemini + formatação
│   └── requirements.txt    # Dependências Python
│
├── frontend/
│   ├── public/
│   │   ├── adidas-furia.png   # Banner da loja FURIA
│   │   ├── bot.png            # Logo da FURIA usada no chatbot
│   │   └── furia-gif.mp4      # Vídeo institucional
│   └── src/
│       ├── components/
│       │   └── Chatbox.jsx
│       ├── styles/
│       │   ├── Chatbox.css
│       │   └── Landing.css
│       └── App.jsx
```


---

## 🚀 Como Rodar o Projeto

### 1. Clone o repositório

git clone https://github.com/seu-usuario/chatbot-furia.git
cd chatbot-furia

### 2. Backend (FastAPI)
Pré-requisitos:
Python 3.10+

Google Gemini API Key

Navegador Google Chrome instalado

**Instalação e execução:**

- cd backend
- python -m venv venv
- source venv/bin/activate | *Windows: .\venv\Scripts\activate*
- pip install -r requirements.txt
- uvicorn main:app --reload

*A API será servida em: http://localhost:8000/chat*

⚠️ **Certifique-se de substituir sua chave Gemini diretamente em responses.py:**

***genai.configure(api_key="SUA_CHAVE_AQUI")***

### 2.1 COMO PEGAR A CHAVE
1. Entre no link -> [LINK](https://ai.google.dev/gemini-api/docs?hl=pt-br)
2. Faça login com seu google
3. Clique em gerar uma chave da API Gemini
4. Desça até o fim da página, clique nos 3 pontos em Ações e Copy Key
5. Cole a chave no local indicado anterioremente

### 3. Frontend (React + Vite)

- Para testes em localhost, alterar o arquivo ChatBox.jsx nas linhas 24 ~ 30
- Alterar const response = await fetch("https://furia-chatbot-qq58.onrender.com/chat"
- Novo valor const response = await axios.post('http://127.0.0.1:8000/chat'
-- Já se encontra no código a linha.
- cd frontend
- npm install
- npm start
- *Acesse o frontend no localhost informado*

---

## 🔐 Endpoints da API

| Método | Rota    | Descrição                                                 |
| ------ | ------- | --------------------------------------------------------- |
| POST   | /chat   | Envia uma mensagem do usuário e retorna a resposta do bot |


## 📚 Exemplo de uso da API

POST /chat

{
  "message": "Quem é o coach da FURIA?"
}

{
  "reply": "Eae, Guerreiro! O coach atual da FURIA é: (Retorno proveniente da liquipedia)"
}

---

## 🛠️ Futuras Melhorias
- Integração com agenda de partidas futuras.
- Interface com múltiplos temas (claro/escuro).
- Otimização do scraping para múltiplas páginas.
- Deploy online (Render, Vercel, ou Railway).

---

## 👨‍💻 Desenvolvedor
***Jhonas Gomes Coutinho de Souza***

Projeto | Desafio Final 1

[LinkedIn](https://www.linkedin.com/in/jhonasgomes/)

---

## 🛒 Links úteis
[FURIA.gg](https://www.furia.gg/)

[Liquipedia - FURIA](https://liquipedia.net/counterstrike/FURIA)

[Google Gemini API](https://ai.google.dev/gemini-api/docs?hl=pt-br)
