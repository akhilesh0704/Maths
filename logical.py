from fastapi import APIRouter 

logical_router = APIRouter()

@logical_router.get("/and") 
async def logical_and(a: bool, b: bool):
     return {"result": a and b}

@logical_router.get("/or")
async def logical_or(a: bool, b:bool):
     return{"result": a or b}

@logical_router.get("/not") 
async def logical_not(a: bool): 
     return {"result": not a}

@logical_router.get("/xor") 
async def logical_xor(a: bool, b: bool): 
     return {"result": (a or b) and not (a and b)}
