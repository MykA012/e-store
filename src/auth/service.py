from datetime import datetime, timedelta, timezone

import jwt
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.ext.asyncio import AsyncSession

from src.auth.security import verify_password
from src.global_deps import session_dep
from src.config import load_auth_jwt
from src.user import user_repo


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login", auto_error=False)


async def auth_user(
    username: str, password: str, session: AsyncSession = Depends(session_dep)
):
    user = await user_repo.get_user_by_username(session, username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        payload=to_encode,
        key=load_auth_jwt().private_key_path.read_text(),
        algorithm=load_auth_jwt().ALGORITHM,
    )
    return encoded_jwt
