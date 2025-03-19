from fastapi import FastAPI
from pydantic import BaseModel
from legalaid_module.searchLawyers import find_relevant_lawyers

app = FastAPI()

class QueryRequest(BaseModel):
    query: str

@app.post("/search")
async def search_lawyers(request: QueryRequest):
    return find_relevant_lawyers(request.query)
