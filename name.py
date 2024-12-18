from fastapi import APIRouter

name_router = APIRouter()

@name_router.get("/name")
async def get_name():
    return {"name": "John Doe"}
