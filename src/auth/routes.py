from datetime import timedelta
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession

from src.user import user_repo
from src.global_deps import session_dep
from src.user.schemas import UserCreate, UserIDB
from src.auth.models import Token
from src.auth.service import auth_user, create_access_token, get_current_active_user

router = APIRouter(tags=["Auth"])


@router.post("/signup")
async def registration(user_in: UserCreate, session=Depends(session_dep)) -> UserIDB:
    user = await user_repo.add_user(session=session, user_in=user_in)
    return user


@router.post("/login")
async def login(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    session: AsyncSession = Depends(session_dep),
) -> Token:
    user = await auth_user(form_data.username, form_data.password, session)
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


@router.get("/me")
async def me(current_user=Depends(get_current_active_user)) -> UserIDB:
    return current_user
