import sys
import os 

from fastapi import FastAPI
from name import name_router
from Akhil.user import user_routergit

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

app.include_router(name_router)

app.include_router(user_router, prefix="/api")
