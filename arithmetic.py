from fastapi import APIRouter 

arithmetic_router = APIRouter()

@arithmetic_router.get("/addition") 
async def addition(a: int, b: int): 
    return {"result": a + b}

@arithmetic_router.get("/multiplication")
async def multiply(a: int, b: int):
    return {"result": a * b}

@arithmetic_router.get("/subtraction")
async def subtraction(a: int, b: int):
    return {"result": a - b}

@arithmetic_router.get("/Division")
async def Division(a: int, b: int):
    return {"result": a / b}

@arithmetic_router.get("/modulus") 
async def modulus(a: int, b: int): 
    return {"result": a % b}