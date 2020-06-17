from fastapi import FastAPI
from pydantic import BaseModel
import os
import subprocess


app = FastAPI()  

class Item(BaseModel):
    code: str

@app.get("/") 
async def root():
    return {"message": "Hello World"}


@app.post("/poster/")
async def create_item(item: Item):
    print(item.code)
    comando = 'sudo docker run python:3.7 python -c ' + item.code
    stream = os.popen(comando)
    output = stream.read()
    print(output)
    return output