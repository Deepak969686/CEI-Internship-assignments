import os
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import RetrievalQA

load_dotenv()


def create_qa_chain(vector_store):

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0.2,
        google_api_key=os.getenv("GOOGLE_API_KEY")
    )

    retriever = vector_store.as_retriever(
        search_kwargs={"k": 3}
    )

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff",
        return_source_documents=True
    )

    return qa_chain


def ask_question(qa_chain, question):
    return qa_chain.invoke({"query": question})