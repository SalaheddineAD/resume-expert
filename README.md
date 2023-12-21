# Resume Expert

## Libraries used
#### PyPDF2
PyPDF2 is an open-source pure-python PDF library capable of splitting, merging, cropping, and transforming the pages of PDF files. It can also add custom data, viewing options, and passwords to PDF files. PyP

#### RecursiveCharacterTextSplitter
Implementation of splitting text that looks at characters.

Recursively tries to split by different characters to find one that works.

It also has the option for overlaping text between chunks.

The reason we are using it is that the context window of LLMs is limited. So we need to split the text into chunks.

#### SentenceSplitter
Sentence splitter that uses a neural network to predict sentence boundaries.
#### Embeddings
Embeddings are a way to represent words as vectors. The idea is that words that are similar will have similar vectors. This is useful for many tasks in NLP, for example, finding synonyms, or in our case, finding similar words to the ones in the resume.

#### FAISS
FAISS is a library for efficient similarity search and clustering of dense vectors. It contains algorithms that search in sets of vectors of any size, up to ones that possibly do not fit in RAM. It also contains supporting code for evaluation and parameter tuning. FAISS is written in C++ with complete wrappers for Python/numpy. Some of the most useful algorithms are implemented on the GPU. It is developed by Facebook AI Research. 
## Instalation
#### creating environment
conda create -n "environment_name"
#### activating environment
conda activate "environment_name"
#### installing requirements
pip install -r requirements.txt

comment:: If you have a problem with installing streamlit check the library altair in requirements.txt

## Usage
#### running the streamlit app
streamlit run app.py
