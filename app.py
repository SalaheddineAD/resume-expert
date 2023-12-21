import streamlit as st
from PyPDF2 import PdfReader
# from stramlit_extras.add_vertical_space import add_vertical_space
from langchain.text_splitter import RecursiveCharacterTextSplitter


#Sidebar contents
with st.sidebar:
    st.title("Resume Expert")
    st.write("Convert PDF to text")
    st.write("by [Langchain](https://langchain.com)")
    st.write("Source code: [Github](https://github.com/SalaheddineAD/resume-expert)")