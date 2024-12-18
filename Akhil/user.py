from fastapi import APIRouter

user_router = APIRouter()

@user_router.get("/user")
async def get_user():
    return {"name": "John Doe"}