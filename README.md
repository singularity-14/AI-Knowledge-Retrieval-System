# AI Knowledge Retrieval System

## Overview
The **AI Knowledge Retrieval System** is a Streamlit-based application that fetches relevant information from Wikipedia or ArXiv papers, stores the data using FAISS embeddings, and utilizes a Large Language Model (LLM) to generate responses based on the retrieved knowledge.

## Features
- Fetches data from **Wikipedia** or **ArXiv Papers**.
- Stores and indexes the retrieved text using **FAISS**.
- Uses **HuggingFace Embeddings** for vector representation.
- Retrieves similar documents based on queries.
- Generates AI-powered responses using **LangChain and LLM from Groq (mixtral-8x7b-32768)**.

## Project Structure
```
📁 AI-Knowledge-Retrieval
│-- backend.py        # Backend functions for data retrieval, embedding, and LLM interaction
│-- app.py            # Streamlit UI for user interaction
│-- .env              # Stores API keys (GROQ_API_KEY)
│-- requirements.txt  # Dependencies
│-- README.md         # Documentation
```

## Installation
1. **Clone the repository**
   ```bash
   git clone https://github.com/your-repo/AI-Knowledge-Retrieval.git
   cd AI-Knowledge-Retrieval
   ```

2. **Create a virtual environment** (optional but recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up API Keys**
   - Create a `.env` file in the project root.
   - Add your **Groq API Key**:
     ```
     GROQ_API_KEY=your_api_key_here
     ```

## Usage
Run the application using Streamlit:
```bash
streamlit run app.py
```

## How It Works
1. The user enters a **topic or question** in the Streamlit UI.
2. The system **fetches relevant data** from Wikipedia or ArXiv.
3. The text is **converted into embeddings** and stored in a **FAISS index**.
4. The **retrieved documents** are passed to a **Large Language Model (LLM)**.
5. The **LLM (mixtral-8x7b-32768) generates a response** based on the stored knowledge.
6. The response is displayed in the UI.

## Technologies Used
- **Python**
- **Streamlit** (UI Framework)
- **FAISS** (Vector Search)
- **LangChain** (LLM Processing)
- **Groq API** (LLM Model [mixtral-8x7b-32768])
- **HuggingFace Embeddings** (Text Vectorization)
- **Wikipedia API** (Data Retrieval)
- **ArXiv API** (Research Papers)

## License
This project is licensed under the MIT License.
