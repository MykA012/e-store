from fastapi import APIRouter, Depends

from src.database.repositories import user_repo
from src.dependencies import session_dep
from src.schemas.user import UserCreate, UserIDB

router = APIRouter()


@router.post("/auth", tags=["Auth"])
async def registration(user_in: UserCreate, session = Depends(session_dep)) -> UserIDB:
    user = await user_repo.create(session=session, user_in=user_in)
    return user


@router.get("/users", tags=["Users"])
async def alL_users(session = Depends(session_dep)) -> list[UserIDB]:
    users = await user_repo.all_users(session=session)
    return users
