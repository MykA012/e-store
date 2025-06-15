from fastapi import APIRouter

from src.auth.router import router as auth_router
from src.user.router import router as user_router

root_router = APIRouter()

root_router.include_router(router=auth_router)
root_router.include_router(router=user_router)
