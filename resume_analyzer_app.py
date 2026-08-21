import streamlit as st

from utils import extract_text_from_pdf, create_vector_text

from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough


# --------------------------------------------------
# Streamlit Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Resume Analyzer RAG",
    page_icon="📄"
)

st.title("Resume Analyzer Ready AI")


# --------------------------------------------------
# User Inputs
# --------------------------------------------------

resume_file = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)

jd_text = st.text_area(
    "Paste Job Description"
)


# --------------------------------------------------
# Analyze Button
# --------------------------------------------------

if st.button("Analyze"):

    if resume_file and jd_text:

        # --------------------------------------------------
        # Step 1: Extract text from Resume PDF
        # --------------------------------------------------

        resume_text = extract_text_from_pdf(resume_file)


        # --------------------------------------------------
        # Step 2: Combine Resume + Job Description
        # --------------------------------------------------

        combine_text = resume_text + "\n\n" + jd_text


        # --------------------------------------------------
        # Step 3: Create Vector Store
        # --------------------------------------------------

        vectorstore = create_vector_text(combine_text)


        # --------------------------------------------------
        # Step 4: Create Retriever
        # --------------------------------------------------

        retriever = vectorstore.as_retriever()


        # --------------------------------------------------
        # Step 5: Load Ollama LLM
        # --------------------------------------------------

        llm = OllamaLLM(
            model="gemma2:2b"
        )


        # --------------------------------------------------
        # Step 6: Create Prompt
        # --------------------------------------------------

        prompt = ChatPromptTemplate.from_template("""
You are an AI Placement Coach.

Analyze the candidate's resume against the given job description.

Context:
{context}

Question:
{question}

Provide the following:

1. Skills Gap Analysis
2. Missing Technologies
3. ATS Score
4. Technical Interview Questions
5. Resume Improvement Suggestions
6. Useful Project Suggestions
7. Complete Roadmap for the Applied Position

Give the answer in a clear and structured format.
""")


        # --------------------------------------------------
        # Step 7: Create RAG Chain
        # --------------------------------------------------

        chain = (
            {
                "context": retriever,
                "question": RunnablePassthrough()
            }
            | prompt
            | llm
            | StrOutputParser()
        )


        # --------------------------------------------------
        # Step 8: Ask Question
        # --------------------------------------------------

        response = chain.invoke(
            "Analyze my resume against the job description."
        )


    

        st.subheader("Analysis Result")

        st.write(response)


    else:

        st.warning(
            "Please upload a resume and provide the job description."
        )