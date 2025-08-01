from flask import Flask, render_template, jsonify, request
from src.helper import download_hugging_face_embeddings
from langchain_pinecone import PineconeVectorStore
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from src.prompt import *
import os
from mu_AiAgent import execute_mu_agent
from langchain_groq import ChatGroq
from flask_cors import CORS
# os.environ["OTEL_SDK_DISABLED"] = "true"

app = Flask(__name__)
CORS(app) 
load_dotenv()

PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')
GROQ_API_KEY=os.environ.get("GROQ_API_KEY")
SERPER_API_KEY = os.environ.get("SERPER_API_KEY")
os.environ['PINECONE_API_KEY']=PINECONE_API_KEY
os.environ["GROQ_API_KEY"]=GROQ_API_KEY
os.environ['SERPER_API_KEY']=SERPER_API_KEY

model=ChatGroq(
        temperature = 0.7,
        model="llama3-70b-8192",
        api_key= os.getenv("GROQ_API_KEY"),
    )
embeddings = download_hugging_face_embeddings()


index_name = "mu-chatbot" 
# Embed each chunk and upsert the embeddings into your Pinecone index.
docsearch = PineconeVectorStore.from_existing_index(
    index_name=index_name,
    embedding=embeddings
)


retriever = docsearch.as_retriever(search_type="similarity", search_kwargs={"k":3})


prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "{input}"),
    ]
)

question_answer_chain = create_stuff_documents_chain(model, prompt)
rag_chain = create_retrieval_chain(retriever, question_answer_chain)


@app.route("/api/mubot", methods=["POST"])
def chat():
    data = request.get_json()  # ✅ handles JSON input
    msg = data.get("msg", "").lower()
    # print(msg)
    # Define keyword triggers for external research agent
    research_keywords = ["research", "latest", "find out", "summarize", "investigate", "report on", "current"]
    # Check if message should trigger research agent
    if any(keyword in msg for keyword in research_keywords):
        try:
            result = execute_mu_agent(msg)
            return jsonify({"answer": result})
        except Exception as e:
            return jsonify({"error": str(e)}), 500
        

     # Otherwise use your existing RAG setup
    try:
        response = rag_chain.invoke({"input": msg})
        return jsonify({"answer": response["answer"]})
    except Exception as e:
        return jsonify({"error": str(e)}), 500



if __name__ == '__main__':
    app.run(host="0.0.0.0", port= 8080, debug= True)