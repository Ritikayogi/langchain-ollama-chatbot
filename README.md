# 🤖 LangChain + Ollama (LLaMA2) GenAI Application

A **local Generative AI application** built using **LangChain**, **Ollama (LLaMA2)**, **FastAPI**, and **Streamlit**.  
This project generates **essays and poems** using a locally running LLM — **no OpenAI, no paid APIs**.

---

## 🌟 Key Features

- 🧠 **LLaMA2 via Ollama** (100% local & free)
- ⚡ **FastAPI backend** with LangServe
- 🎨 **Streamlit frontend** for user interaction
- ✍️ Generates:
  - Essays
  - Child-friendly poems
- 🔐 Secure Git setup (no secrets pushed)
- 💻 Runs completely on local machine

---

## 🛠️ Tech Stack

- Python  
- LangChain  
- LangServe  
- Ollama (LLaMA2)  
- FastAPI  
- Streamlit  
- Uvicorn  
- Git & GitHub  

---

## 📁 Project Structure

LANGCHAIN/
│
├── api/
│ └── app.py # FastAPI backend (LangChain + Ollama)
│
├── client.py # Streamlit frontend
├── .gitignore # Ignored files (venv, .env, cache)
├── README.md
└── venv/ # Virtual environment (ignored)


---

## ⚙️ Setup & Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Ritikayogi/langchain-ollama-chatbot.git
cd langchain-ollama-chatbot
```
###2️⃣ Create & Activate Virtual Environment (Windows)
python -m venv venv
venv\Scripts\activate
3️⃣ Install Dependencies
pip install langchain==0.1.16 langserve==0.0.51 langchain-community fastapi uvicorn streamlit requests
4️⃣ Install Ollama & LLaMA2

Download Ollama from:
https://ollama.com

Pull the model:
ollama pull llama2
▶️ Running the Application
🔹 Start Backend (FastAPI)
cd api
python app.py
API: http://localhost:8000

Swagger Docs: http://localhost:8000/docs

🔹 Start Frontend (Streamlit)

Open a new terminal (venv activated):

streamlit run client.py


App URL: http://localhost:8501
