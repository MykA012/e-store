from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from src.auth.security import get_password_hash
from src.cart.cart_repo import create_user_cart
from src.user.models import User
from src.user.schemas import (
    UserCreate,
    UserEdit,
    UserChangePassword,
)


async def create_user(
    session: AsyncSession,
    user_in: UserCreate,
) -> User:
    user = User(
        username=user_in.username,
        email=user_in.email,
        hashed_password=get_password_hash(user_in.hashed_password),
    )
    session.add(user)
    await session.commit()
    await session.refresh(user)
    await create_user_cart(
        session=session,
        user=user,
    )

    return user


async def get_user_by_email(
    session: AsyncSession,
    email: str,
) -> User | None:
    stmt = select(User).where(User.email == email)
    result = await session.execute(stmt)
    return result.scalar_one_or_none()


async def edit_user(
    session: AsyncSession,
    user: User,
    edit_user: UserEdit,
) -> User:
    for name, value in edit_user.model_dump(exclude_unset=True).items():
        setattr(user, name, value)

    await session.commit()
    await session.refresh(user)
    return user


async def change_user_password(
    session: AsyncSession,
    user: User,
    edit_pass: UserChangePassword,
) -> User:
    user.hashed_password = get_password_hash(
        edit_pass.hashed_password,
    )

    await session.commit()
    await session.refresh(user)
    return user


async def delete_user(
    session: AsyncSession,
    user: User,
) -> None:
    await session.delete(user)
    await session.commit()
