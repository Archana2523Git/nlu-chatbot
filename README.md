# NLP Chatbot with Local LLM (Ollama) 🤖🧠

📌 **Project Overview**  
This is a locally hosted NLP chatbot system that uses a **custom NLU model** for intent classification and a **local LLM via Ollama** for context-aware responses. The project has a **Python backend** for NLU/LLM processing and a **React frontend** for an interactive chat interface.

It runs completely offline—no external API keys are required.

---

## 🧩 Architecture

```text
User Input (Frontend)
       ↓
Intent Classifier (Python NLU)
       ↓
Intent-aware Prompt
       ↓
Ollama Local LLM
       ↓
Response Display (Frontend)
🚀 Features

Intent classification using labeled datasets

Local LLM inference (offline, secure, no cloud API)

Interactive React frontend for chatting with the bot

Modular design for adding new intents or LLM logic

Easy evaluation of intent classification accuracy

🛠️ Tech Stack

Frontend: React, Vite, HTML, CSS, JavaScript

Backend: Python 3.10+, Streamlit (optional), Ollama, Scikit-learn

Database: JSON-based datasets (intents.json, eval_dataset.json)

Version Control: Git & GitHub

📂 Project Structure
nlp-chatbot/
│
├── backend/
│   ├── main.py              # Main backend entry
│   ├── requirements.txt     # Python dependencies
│   ├── nlu/                 # Custom NLU model logic
│   ├── services/            # Additional backend services
│   └── venv/                # Python virtual environment
│
├── frontend/
│   ├── src/                 # React source code
│   ├── public/              # Static files
│   ├── index.html           # Main HTML
│   ├── package.json         # Node dependencies
│   ├── package-lock.json
│   ├── vite.config.js
│   └── README.md
│
└── README.md
⚙️ Setup Instructions
1️⃣ Backend Setup
cd backend
python -m venv venv          # Create virtual environment
venv\Scripts\activate        # Activate (Windows)
# or source venv/bin/activate  # macOS/Linux
pip install -r requirements.txt

Start backend server (example):

python main.py
2️⃣ Frontend Setup
cd frontend
npm install                  # Install Node dependencies
npm run dev                  # Start React frontend

Open your browser at http://localhost:5173 (default Vite port) to interact with the bot.

🧪 Evaluation

Evaluate NLU intent classification using your test dataset.

Backend will provide predicted intents and LLM responses.

Metrics include accuracy and optional confusion matrix (if implemented).

🔮 Future Improvements

Multi-intent handling

Conversation context memory across messages

Fine-tuning the LLM locally for domain-specific intents

Docker-based deployment for easy sharing
