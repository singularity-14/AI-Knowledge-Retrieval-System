# Essential Libraries
import time
import streamlit as st
from backend import *
# Streamlit UI Setup
st.set_page_config(page_title="AI Knowledge Retrieval", layout="wide")
st.title("📚 AI Knowledge Retrieval System")

# User Inputs
query = st.text_input("🔍 Enter a topic or question:")
data_source = st.selectbox("📂 Choose a Data Source:", ["Wikipedia", "ArXiv Papers"])
fetch_data_btn = st.button("📥 Fetch Data")

# Fetching Data
retrieved_data = ""
if fetch_data_btn and query:
    st.write("🔄 Fetching relevant data...")
    
    if data_source == "Wikipedia":
        retrieved_data = fetch_wikipedia_text(query)
    else:
        retrieved_data = fetch_arxiv_papers(query, max_results=2)

    if retrieved_data:
        store_embeddings([retrieved_data[0:1000]])
        st.success("✅ Data successfully retrieved and stored in FAISS!")
        print(retrieved_data)
        # Generate AI response immediately after data retrieval
        with st.spinner("🧠 Generating AI Response..."):
            ai_response = generate_response(query)  # Pass retrieved data to LLM
            st.write(ai_response)
            st.success("✅ AI Response Generated!")
    else:
        st.error("⚠️ No data found for the given query.")
