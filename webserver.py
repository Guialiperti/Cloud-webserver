from fastapi import FastAPI
from pydantic import BaseModel
import os
import subprocess


app = FastAPI()  

class Item(BaseModel):
    message: str

@app.get("/") 
async def root():
    return {"message": "Hello World"}


@app.post("/poster")
async def create_item(item: Item):
    return item