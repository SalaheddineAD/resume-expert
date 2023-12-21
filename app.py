import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
import pickle
import os

# Header
st.header("Improve your resume and get x2 more interviews! ")

# File uploader
pdf = st.file_uploader("Upload your PDF file", type='pdf')

#Sidebar contents
with st.sidebar:
    st.title("Resume Expert")
    st.write("Convert PDF to text")
    st.write("by [Langchain](https://langchain.com)")
    st.write("Source code: [Github](https://github.com/SalaheddineAD/resume-expert)")
    st.markdown(
        """
        This is an LLM-based application that allows you to enhance your resume and double your chances of getting a job. 
        The LLM has been trained on a great number of resumes that have known huge success.
        """
    )

# When user uploads pdf 
if pdf is not None:
    #red pdf
    pdf_reader = PdfReader(pdf)

    #convert pdf to text
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    st.write(text)

    #split text
    splitter = RecursiveCharacterTextSplitter(
        chunk_size = 1000,
        max_splits=10
    )
    chunks = splitter.split_text(text)

    #embed chunks
    embedder = OpenAIEmbeddings()
    embeddings = embedder.embed_text(chunks)

    #check if the pdf is already in the database

    #selecting the name of the pdf without ".pdf"
    pdf_name = pdf.name[:-4]

    if(pdf_name in os.path("vector_database"))

    #create vector store
    vectorStore = FAISS.from_texts(chunks, embedding=embeddings)
    # check if the pdf is already in the database 
    with open(f"vector_database/{pdf_name}.pkl","wb") as f:
        pickle.dump(embeddings,f)


    #get most similar chunks
    query = "I am a software engineer"
    query_embedding = embedder.embed_text(query)
    results = vectorStore.most_similar(query_embedding, 5)




def main():
    st.write("hello")

if __name__ == "__main__":
    main()