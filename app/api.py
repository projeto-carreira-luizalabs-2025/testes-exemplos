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

class SampleResponse(BaseModel):
    chave: str
    valor: int | str

@app.get("/sample")
async def get_sample() -> SampleResponse:
    
    sample_response = SampleResponse(chave="chave01", valor=1)
    return sample_response