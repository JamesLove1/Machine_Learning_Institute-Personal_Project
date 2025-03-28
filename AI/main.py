from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

from mnist_model.modelWebService import modelWebService

app = FastAPI()

class Data(BaseModel):
    img: list[list[list[int]]]
    num: str

@app.post("/")
def read_root(requestBody: Data):
    
    predictedNum, predictionConfidence = modelWebService(requestBody)
    response = {
        "predictedNum":predictedNum, 
        "predictionConfidence": predictionConfidence
    }
    
    return response
