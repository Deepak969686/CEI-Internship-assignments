import uuid
from langchain_chroma import Chroma

DB_DIRECTORY = "chroma_db"


def create_vector_store(chunks, embeddings):
    """
    Create a new Chroma vector database with a unique folder
    for every uploaded PDF.
    """

    db_path = f"{DB_DIRECTORY}/{uuid.uuid4()}"

    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=db_path
    )

    return vector_store


def load_vector_store(db_path, embeddings):
    """
    Load an existing Chroma vector database.
    """

    vector_store = Chroma(
        persist_directory=db_path,
        embedding_function=embeddings
    )

    return vector_store