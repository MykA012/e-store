from fastapi import APIRouter

from src.auth.routes import router as auth_router
from src.user.routes import router as user_router

root_router = APIRouter()

root_router.include_router(router=auth_router)
root_router.include_router(router=user_router)
