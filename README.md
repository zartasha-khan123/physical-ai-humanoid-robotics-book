"# physical-ai-humanoid-robotics-book" 

📘 Physical AI & Humanoid Robotics Book
With Integrated RAG AI Chatbot

An interactive, AI-powered technical book focused on Physical AI, Embodied Intelligence, and Humanoid Robotics, enhanced with a Retrieval-Augmented Generation (RAG) chatbot that allows readers to ask questions directly from the book content.

This project combines modern documentation tooling, AI agents, and vector databases to deliver a next-generation learning experience.

🚀 Live Demo

📚 Book Website (Docusaurus + Vercel)
👉 Deployed on Vercel

🤖 RAG Chatbot
Embedded directly into the book UI, capable of:

Answering questions about the book

Answering questions based on user-selected text only

Citing sources from the book content

🧠 Key Features
📖 Book Platform

Built using Docusaurus

Clean, responsive UI

Markdown-based content

Deployed on Vercel

🤖 Integrated RAG Chatbot

Retrieval-Augmented Generation (RAG)

Answers strictly from book content

Optional selected-text-only answering

Source-aware responses

⚙️ Backend (FastAPI)

Modular FastAPI architecture

REST API for chatbot queries

CORS enabled for frontend integration

OpenAI-powered LLM responses

🧠 AI & Vector Search

OpenAI GPT models for reasoning

OpenAI Embeddings for vectorization

Qdrant Cloud (Free Tier) as vector database

Efficient semantic search over book content

🏗️ Tech Stack
Frontend

Docusaurus

React

CSS

Vercel (Deployment)

Backend

FastAPI

Python 3.10+

OpenAI API

Qdrant Cloud

AI / RAG

OpenAI Chat Completions

OpenAI Embeddings

Vector similarity search

Context-restricted answering

📂 Project Structure
physical-ai-humanoid-robotics-book/
│
├── docusaurus-book/          # Frontend (Book + Chatbot UI)
│   ├── src/
│   │   ├── components/
│   │   │   ├── Chatbot.jsx
│   │   │   └── Chatbot.css
│   │   └── pages/
│   └── docs/
│
├── rag_backend/              # Backend (FastAPI + RAG)
│   ├── app/
│   │   ├── main.py
│   │   ├── rag.py
│   │   ├── config.py
│   │   └── __init__.py
│   ├── ingest/
│   │   └── ingest_docs.py
│   ├── .env
│   └── requirements.txt
│
└── README.md

⚙️ Environment Variables

Create a .env file inside rag_backend/:

OPENAI_API_KEY=your_openai_api_key
QDRANT_URL=https://your-qdrant-url
QDRANT_API_KEY=your-qdrant-api-key

▶️ Running the Project Locally
1️⃣ Backend (FastAPI)
cd rag_backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload


Backend will run at:

http://127.0.0.1:8000


API docs:

http://127.0.0.1:8000/docs

2️⃣ Frontend (Docusaurus)
cd docusaurus-book
npm install
npm start


Frontend will run at:

http://localhost:3000

🔍 How the RAG Chatbot Works

Book content is split into chunks

Chunks are embedded using OpenAI embeddings

Vectors are stored in Qdrant

User asks a question (optionally selects text)

Relevant chunks are retrieved

LLM answers only using retrieved context

This ensures:

❌ No hallucinations

✅ Accurate, book-based answers

✅ Transparent source usage

🎯 Use Cases

AI & Robotics education

Interactive technical books

AI-powered documentation

Knowledge-based chatbots

Hackathons & academic projects

🧪 Status

✅ Book written & deployed

✅ RAG backend implemented

✅ Qdrant integration complete

✅ Chatbot embedded in UI

🔄 Continuous improvements ongoing

🙌 Acknowledgements

OpenAI

Qdrant

Docusaurus

FastAPI

Vercel

📜 License

This project is for educational and research purposes.

👤 Author

Zartash Imran
AI Developer | Web Developer | UI/UX Designer
Focused on AI Agents, RAG Systems & Intelligent Applications
