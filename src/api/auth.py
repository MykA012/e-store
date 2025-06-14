from datetime import timedelta
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession

from src.database.models.user import User
from src.database.repositories import user_repo
from src.dependencies import session_dep
from src.schemas.user import UserCreate, UserIDB
from src.auth.models import Token
from src.auth.service import auth_user, create_access_token, get_current_active_user

router = APIRouter()


@router.post("/signup", tags=["Auth"], summary="Создает нового пользователя в бд")
async def registration(user_in: UserCreate, session=Depends(session_dep)) -> UserIDB:
    user = await user_repo.create(session=session, user_in=user_in)
    return user


@router.post("/login", tags=["Auth"])
async def login(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    session: AsyncSession = Depends(session_dep),
) -> Token:
    user = auth_user(form_data.email, form_data.password, session)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=1440)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")


@router.get("/me", tags=["Debug"])
async def me(current_user: User = Depends(get_current_active_user)) -> UserIDB:
    return current_user


@router.get("/users", tags=["Debug"])
async def alL_users(session=Depends(session_dep)) -> list[UserIDB]:
    users = await user_repo.all_users(session=session)
    return users
