from fastapi import FastAPI
from pydantic import BaseModel, Field


app = FastAPI(title="App", version="0.0.1")

class RootResponse(BaseModel):
    version: str = Field(app.version)
    
    
async def foo():
    print("Faça algo por mim...")
    
@app.get("/")
async def get_root() -> RootResponse:
    await foo()
    resp = {}
    return resp
