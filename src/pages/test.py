import streamlit as st
import pickle
from langchain.document_loaders import UnstructuredURLLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores.faiss import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.chains import RetrievalQAWithSourcesChain
from langchain import OpenAI
from dotenv import find_dotenv, load_dotenv
import os
from langchain.chat_models import ChatOpenAI

load_dotenv(find_dotenv())
OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]

# Function to load the vector store from the disk
def load_vector_store(filename):
    with open(filename, "rb") as f:
        return pickle.load(f)

# Function to process the URLs and get responses from the model
def process_urls(urls, question):
    # Load the URLs data
    loaders = UnstructuredURLLoader(urls=urls)
    data = loaders.load()

    # Split documents
    text_splitter = CharacterTextSplitter(separator='\n', chunk_size=1000, chunk_overlap=200)
    docs = text_splitter.split_documents(data)

    # Load vector store
    VectorStore = load_vector_store("faiss_store_openai.pk1")

    # Create the retrieval chain
    chain = RetrievalQAWithSourcesChain.from_llm(llm=llm, retriever=VectorStore.as_retriever())

    # Ask the question
    response = chain({"question": question}, return_only_outputs=True)

    return response

# Load the vector store and model
VectorStore = load_vector_store("faiss_store_openai.pk1")
llm = ChatOpenAI()

# Streamlit app
def main():
    # Page title
    st.title("Webpage Question Answering")

    # User input for multiple URLs
    st.subheader("Enter URLs (one URL per line):")
    user_urls = st.text_area("Paste URLs here, one per line")

    # Split user input into a list of URLs
    urls = user_urls.strip().split("\n")

    # User input for the question
    st.subheader("Enter your question:")
    question = st.text_input("Question", "Can you summarize this website?")



    if st.button("Process URLs"):
        # Process URLs and get response
        with st.spinner("Processing URLs and answering question..."):
            response = process_urls(urls, question)
        st.success("Answer:")
        st.write(response)

if __name__ == "__main__":
    main()
