import math
from fastapi import FastAPI
from arithmetic import arithmetic_router
from algebric import algebric_router
from logical import logical_router



app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to Easy Maths"}

app.include_router(arithmetic_router, prefix="/api")
app.include_router(algebric_router, prefix="/api")
app.include_router(logical_router, prefix="/api")