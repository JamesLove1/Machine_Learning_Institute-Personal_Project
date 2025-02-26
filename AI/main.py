from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

class Data(BaseModel):
    img: list[list[list[int]]]
    realNumber: str

@app.post("/")
def read_root(requestBody: dict):
    
    
    print(requestBody.keys())
    
    return {"Hello": "World"}
