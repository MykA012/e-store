from fastapi import APIRouter, Depends

from src.global_deps import session_dep
from src.user.schemas import UserIDB
from src.user import user_repo

router = APIRouter(tags=["users"])


@router.get("/users")
async def alL_users(session=Depends(session_dep)) -> list[UserIDB]:
    users = await user_repo.all_users(session=session)
    return users
