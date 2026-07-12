import os
import streamlit as st

from src.loader import load_pdf
from src.splitter import split_documents
from src.embeddings import load_embedding_model
from src.vector_store import create_vector_store
from src.rag_pipeline import create_qa_chain, ask_question

st.set_page_config(
    page_title="Document Question Answering (RAG)",
    page_icon="📚",
    layout="wide"
)

st.title("📚 Document Question Answering System")
st.write("Upload a PDF and ask questions about it.")

# -------------------------
# Session State
# -------------------------
if "qa_chain" not in st.session_state:
    st.session_state.qa_chain = None

if "uploaded_pdf" not in st.session_state:
    st.session_state.uploaded_pdf = None

# -------------------------
# Upload PDF
# -------------------------
uploaded_file = st.file_uploader(
    "Choose a PDF",
    type=["pdf"]
)

if uploaded_file is not None:

    # Process only if a NEW PDF is uploaded
    if st.session_state.uploaded_pdf != uploaded_file.name:

        st.session_state.uploaded_pdf = uploaded_file.name

        os.makedirs("data", exist_ok=True)

        # Remove old PDFs
        for file in os.listdir("data"):
            if file.endswith(".pdf"):
                os.remove(os.path.join("data", file))

        pdf_path = os.path.join("data", uploaded_file.name)

        with open(pdf_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        with st.spinner("Processing PDF..."):

            documents = load_pdf(pdf_path)

            chunks = split_documents(documents)

            embeddings = load_embedding_model()

            vector_store = create_vector_store(
                chunks,
                embeddings
            )

            st.session_state.qa_chain = create_qa_chain(
                vector_store
            )

        st.success("PDF processed successfully!")

# -------------------------
# Ask Questions
# -------------------------
if st.session_state.qa_chain is not None:

    st.subheader("Ask Questions")

    question = st.text_input(
        "Enter your question"
    )

    if st.button("Get Answer"):

        if question.strip() == "":
            st.warning("Please enter a question.")

        else:

            with st.spinner("Generating answer..."):

                result = ask_question(
                    st.session_state.qa_chain,
                    question
                )

            st.subheader("Answer")

            st.write(result["result"])

            st.subheader("Retrieved Context")

            for i, doc in enumerate(
                result["source_documents"],
                start=1
            ):

                with st.expander(f"Chunk {i}"):

                    st.write(doc.page_content)

                    st.caption(doc.metadata)