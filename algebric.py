from fastapi import APIRouter 

algebric_router = APIRouter()

@algebric_router.get("/square") 
async def square(a: float,): 
    return {"result": a * a}

@algebric_router.get("/cube_root")
async def cube_root(a: float):
    return{"result": a ** 1/3}

@algebric_router.get("/quartic_root")
async def quartic_root(a: float): 
    return {"result": a ** (1/4)}

@algebric_router.get("/exponentiation") 
async def exponentiation(base: float, exponent: float):
    return {"result": base ** exponent}

@algebric_router.get("/square_root") 
async def square_root(a: float): 
    return {"result": a ** 0.5}

@algebric_router.get("/nth_root")
async def nth_root(a: float, n: float): 
    return {"result": a ** (1/n)}

@algebric_router.get("/logarithm") 
async def logarithm(a: float, base: float):
    return {"result": log(a, base)}

@algebric_router.get("/factorial") 
async def factorial_endpoint(a: int):
     if a < 0:
         return {"error": "Factorial is not defined for negative numbers"} 
     return {"result": factorial(a)}