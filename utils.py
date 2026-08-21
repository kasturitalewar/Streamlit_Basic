from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.documents import Document
from pypdf import PdfReader


# --------------------------------------------------
# RAG STEP 1: Document Loading
# --------------------------------------------------

def extract_text_from_pdf(file):

    reader = PdfReader(file)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text

    return text


# --------------------------------------------------
# RAG STEP 2: Data Splitting
# --------------------------------------------------

def split_text(text):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    return splitter.split_text(text)


# --------------------------------------------------
# RAG STEP 3: Data Embedding + Vector Store
# --------------------------------------------------

def create_vector_text(text):

    chunks = split_text(text)

    docs = [
        Document(page_content=chunk)
        for chunk in chunks
    ]

    embeddings = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2"
    )

    vectorstore = FAISS.from_documents(
        docs,
        embedding=embeddings
    )

    return vectorstore