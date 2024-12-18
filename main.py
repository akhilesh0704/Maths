import sys
import os 

from fastapi import FastAPI
from name import name_router

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

app.include_router(name_router)
