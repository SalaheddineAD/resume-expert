import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS

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

    vectorStore = FAISS.from_texts(chunks, embedding=embeddings)
    st.write(chunks)



def main():
    st.write("hello")

if __name__ == "__main__":
    main()