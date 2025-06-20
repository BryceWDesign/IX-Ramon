"""
IX-Ramon REST API Server

Exposes endpoints for real-time mathematical and cryptographic question handling.
Part of the IX-Gibson distributed AI framework.
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn
from core.query_processor import IXRamonQueryProcessor

app = FastAPI()
query_processor = IXRamonQueryProcessor()

class QueryRequest(BaseModel):
    query: str

@app.post("/query")
async def handle_query(request: QueryRequest):
    if not request.query or request.query.strip() == "":
        raise HTTPException(status_code=400, detail="Query must not be empty.")
    try:
        answer = query_processor.process_query(request.query)
        return {"answer": answer}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal error: {str(e)}")

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8010)
