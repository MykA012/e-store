from datetime import timedelta
from typing import Annotated

from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import (
    APIRouter, Depends,
    HTTPException, status,
    Response,
)

from src.auth.service import auth_user, create_access_token
from src.user.schemas import UserCreate, UserIDB
from src.global_deps import session_dep
from src.auth.models import Token
from src.user import user_repo

router = APIRouter(tags=["Auth"])


@router.post("/signup")
async def registration(
    user_in: UserCreate,
    session=Depends(session_dep),
) -> UserIDB:
    user = await user_repo.create_user(
        session=session,
        user_in=user_in,
    )
    return user


@router.post("/login")
async def login(
    response: Response,
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    session: AsyncSession = Depends(session_dep),
) -> Token:
    user = await auth_user(form_data.username, form_data.password, session)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=1440)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    response.set_cookie(
        key="access_token",
        value=f"Bearer {access_token}",
        httponly=True,
        max_age=int(access_token_expires.total_seconds()),
        secure=True,
        samesite="lax",
    )

    return Token(access_token=access_token, token_type="bearer")


@router.post("/logout")
async def logout(
    response: Response
):
    response.delete_cookie(
        key="access_token",
        path="/",
        domain="localhost",
    )
    return {"status": 200, "message": "Successfully logged out"}
