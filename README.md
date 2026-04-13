# 🧠 AI Knowledge Retrieval System

> A RAG-powered research assistant that fetches real-time knowledge from Wikipedia and ArXiv, indexes it with FAISS vector search, and generates accurate answers using Mixtral-8x7B on Groq — all through a clean Streamlit interface.

---

## 📌 Project Overview

Traditional LLMs are limited to their training data. This project solves that by building a **dynamic knowledge retrieval pipeline** — the system fetches up-to-date content from Wikipedia or ArXiv at query time, embeds it into a FAISS vector store, and uses an LLM to generate grounded, source-backed answers.

Great for research queries, literature exploration, and understanding cutting-edge papers without leaving the app.

---

## ✨ Key Features

| Feature | Description |
|---------|-------------|
| 🌐 Live data sources | Fetches real-time content from Wikipedia and ArXiv |
| 🔍 Semantic search | FAISS vector index for fast similarity-based retrieval |
| 🤗 HuggingFace embeddings | Open-source text vectorization — no OpenAI dependency |
| 🤖 LLM-powered answers | Mixtral-8x7B on Groq generates responses grounded in retrieved docs |
| ⚡ Low-latency inference | Groq API delivers near-instant LLM responses |
| 🖥️ Interactive UI | Clean Streamlit interface for seamless user interaction |

---

## 🚀 Tech Stack

| Category | Tools |
|----------|-------|
| Language | Python 3.8+ |
| LLM | Mixtral-8x7B-32768 (via Groq) |
| RAG Framework | LangChain |
| Vector Database | FAISS |
| Embeddings | HuggingFace Sentence Transformers |
| Data Sources | Wikipedia API, ArXiv API |
| Frontend | Streamlit |
| Config | python-dotenv |

---

## 🏗️ How It Works

```
User enters a topic or question
        ↓
Fetch relevant content
  ├── Wikipedia API
  └── ArXiv Papers API
        ↓
Chunk & embed text
  └── HuggingFace Embeddings → FAISS Vector Index
        ↓
Semantic retrieval of most relevant chunks
        ↓
Retrieved context + query → Mixtral-8x7B (Groq)
        ↓
Grounded, accurate response displayed in UI
```

---

## ⚙️ Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/AI-Knowledge-Retrieval.git
cd AI-Knowledge-Retrieval
```

### 2. Create a virtual environment (recommended)
```bash
python -m venv venv
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root:
```bash
GROQ_API_KEY=your_groq_api_key_here
```
> Get your free Groq API key at [console.groq.com](https://console.groq.com)

### 5. Run the application
```bash
streamlit run app.py
```
Visit `http://localhost:8501` in your browser.

---

## 📂 Project Structure

```
AI-Knowledge-Retrieval/
│
├── app.py              # Streamlit UI — user input, query flow, response display
├── backend.py          # Core logic — data fetching, embedding, FAISS indexing, LLM calls
├── requirements.txt    # Python dependencies
├── .env                # API keys (not committed to version control)
└── README.md           # Project documentation
```

---

## 💡 Key Learnings & Takeaways

- Built a **retrieval-augmented generation (RAG) pipeline** that grounds LLM responses in live, external data
- Used **HuggingFace open-source embeddings** as a cost-free alternative to proprietary embedding APIs
- Integrated **multiple data source APIs** (Wikipedia + ArXiv) with a unified retrieval interface
- Leveraged **Groq's inference speed** to keep end-to-end latency low despite multi-step pipeline

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

*Exploring dynamic knowledge grounding for LLMs using open-source tools and real-time data retrieval.*
