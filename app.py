import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from dotenv import load_dotenv
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
    # st.write(text)

    #split text
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )
    chunks = splitter.split_text(text)

    #selecting the name of the pdf without ".pdf"
    pdf_name = pdf.name[:-4]

    # loading the variables of the .env file
    load_dotenv(dotenv_path=".", verbose=True)
    #Initialize embeddings
    embeddings = OpenAIEmbeddings(openai_api_key="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")

    #check if the pdf is already in the database
    if os.path.exists(f"{pdf_name}"):
        FAISS.load_local(f"vecor_db/{pdf_name}", embeddings)
    else:
        #create vector store
        vectorStore = FAISS.from_texts(chunks, embedding=embeddings)
        #create vector store
        vectorStore.save_local(f"vector_db/{pdf_name}")
    
    query = st.text_input("Ask a question about your pdf")
    st.write(query)



def main():
    pass

if __name__ == "__main__":
    main()