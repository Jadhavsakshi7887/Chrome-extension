# api.py
from fastapi import FastAPI
from pydantic import BaseModel
from rag_query import rag_query
from vectorstore_manager import initialize_vectorstore

app = FastAPI(title="RAG Bot API")

# ---------------- Initialize vectorstore once ----------------
pdf_path = "C:\\Users\\Dell\\Downloads\\SakshiJadhavResume (1).pdf"
initialize_vectorstore(pdf_path)

# ---------------- Request model ----------------
class Query(BaseModel):
    message: str

# ---------------- POST endpoint ----------------
@app.post("/chat")
async def chat(query: Query):
    """
    Receives a question from the client and returns the RAG bot answer.
    """
    answer = rag_query(query.message)
    return {"reply": answer}
