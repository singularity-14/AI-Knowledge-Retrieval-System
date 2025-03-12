# Essential Libraries
import os
import wikipediaapi
import arxiv
import faiss
import numpy as np
import logging
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.chains.question_answering import load_qa_chain
from langchain.docstore.document import Document

# Set up logging
logging.basicConfig(filename="retrieval_system.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

load_dotenv()

# Load Groq API Key
groq_api_key = os.getenv("GROQ_API_KEY")

# Initialize Wikipedia API with proper user agent
wiki = wikipediaapi.Wikipedia(user_agent="MyAIApp/1.0", language="en")

# Initialize Embedding Model
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# FAISS Index
embedding_dim = 384  # Dimension of MiniLM embeddings
index = faiss.IndexFlatL2(embedding_dim)
stored_texts = []

def fetch_wikipedia_text(topic):
    """Fetch Wikipedia content based on a given topic."""
    try:
        page = wiki.page(topic)
        if page.exists():
            logging.info(f"Fetched Wikipedia page for: {topic}")
            return page.text
        else:
            logging.warning(f"Wikipedia page not found: {topic}")
            return None
    except Exception as e:
        logging.error(f"Error fetching Wikipedia page: {str(e)}")
        return None

def fetch_arxiv_papers(query, max_results=2):
    """Fetch ArXiv paper abstracts based on a given query."""
    try:
        search = arxiv.Search(query=query, max_results=max_results, sort_by=arxiv.SortCriterion.Relevance)
        papers = []
        for result in search.results():
            papers.append(f"Title: {result.title}\nAbstract: {result.summary}")
        logging.info(f"Fetched {len(papers)} ArXiv papers for query: {query}")
        return papers
    except Exception as e:
        logging.error(f"Error fetching ArXiv papers: {str(e)}")
        return []

def store_embeddings(texts):
    """Convert texts to embeddings and store in FAISS index."""
    global stored_texts
    try:
        vectors = [embedding_model.embed_query(text) for text in texts]
        vectors = np.array(vectors).astype("float32")
        index.add(vectors)
        stored_texts.extend(texts)
        logging.info(f"Stored {len(texts)} documents in FAISS index.")
    except Exception as e:
        logging.error(f"Error storing embeddings: {str(e)}")

def retrieve_similar_documents(query):
    """Retrieve most relevant documents based on query."""
    try:
        query_vector = np.array([embedding_model.embed_query(query)]).astype("float32")
        distances, indices = index.search(query_vector,k=5)
        retrieved_docs = [stored_texts[i] for i in indices[0] if i < len(stored_texts)]
        logging.info(f"Retrieved {len(retrieved_docs)} relevant documents for query: {query}")
        return retrieved_docs
    except Exception as e:
        logging.error(f"Error retrieving documents: {str(e)}")
        return []

def generate_response(query):
    """Retrieve documents and generate AI-based response."""
    retrieved_docs = retrieve_similar_documents(query)
    if not retrieved_docs:
        return "No relevant information found."

    # Convert documents to LangChain format
    documents = [Document(page_content=doc) for doc in retrieved_docs]
    print(documents)
    
    try:
        prompt = f"""Summarize the content and generate response based on previded documents.\n
                    User Query: {query}"""
        llm = ChatGroq(groq_api_key=groq_api_key, temperature=0.3)
        qa_chain = load_qa_chain(llm, chain_type="stuff")
        response = qa_chain.run(input_documents=documents, question=prompt)
        logging.info(f"Generated AI response for query: {query}")
        return response
    except Exception as e:
        logging.error(f"Error generating AI response: {str(e)}")
        return "An error occurred while generating the response."
