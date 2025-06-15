from fastapi import APIRouter, Depends

from src.auth.service import get_current_active_user
from src.global_deps import session_dep
from src.user.schemas import UserIDB
from src.user.models import User
from src.user import crud

router = APIRouter()


@router.get("/me", tags=["Debug"])
async def me(current_user: User = Depends(get_current_active_user)) -> UserIDB:
    return current_user


@router.get("/users", tags=["Debug"])
async def alL_users(session=Depends(session_dep)) -> list[UserIDB]:
    users = await crud.all_users(session=session)
    return users
