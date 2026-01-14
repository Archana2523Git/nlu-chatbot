# NLU Chatbot with Local LLM (Ollama)

## 📌 Project Overview
This project is an **NLU-based chatbot system** that combines:
- **Intent Classification** using a custom NLU model
- **Local LLM inference** using **Ollama**
- **Interactive UI** built with **Streamlit**

The system first identifies the **user’s intent**, then generates a **context-aware response** using a locally hosted LLM.

---

## 🧠 Architecture
User Input  
→ Intent Classifier (NLU)  
→ Intent-aware Prompt  
→ Ollama (Local LLM)  
→ Response Display (Streamlit)

---

## 🚀 Features
- Intent classification using labeled intent dataset
- Local LLM inference (no cloud API)
- Streamlit-based interactive dashboard
- Evaluation using test dataset
- Modular and extensible design

---

## 🛠️ Tech Stack
- Python 3.10+
- Streamlit
- Ollama
- Scikit-learn
- JSON-based datasets

---

## 📂 Project Structure
nlu_chatbot/
│
├── app.py # Streamlit UI
├── llm_nlu.py # NLU + LLM logic
├── ollama_client.py # Ollama interface
├── evaluate.py # Model evaluation
├── requirements.txt
├── data/
│ ├── intents.json
│ ├── eval_dataset.json
│
└── README.md

yaml
Copy code

---

## ⚙️ Setup Instructions

### 1️⃣ Create Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate
2️⃣ Install Dependencies
bash
Copy code
pip install -r requirements.txt
3️⃣ Start Ollama
bash
Copy code
ollama serve
Ensure at least one model is available:

bash
Copy code
ollama list
▶️ Run the Application
bash
Copy code
streamlit run app.py
🧪 Evaluation
Run evaluation script to test intent classification accuracy:

bash
Copy code
python evaluate.py
📊 Output
Predicted intent

Intent-aware LLM response

Evaluation metrics (accuracy, confusion matrix)

🔮 Future Improvements
Multi-intent handling

Context memory across conversations

Model fine-tuning

Deployment using Docker

👤 Author
Archana

📝 Notes
This project runs entirely locally

No external API keys required

Designed for academic evaluation and demonstration

yaml
Copy code

---

## What to do now (no excuses)
1. Save this as `README.md` inside `nlu_chatbot`
2. Run:
```bat
git add README.md
git commit -m "Add project README"
git push
