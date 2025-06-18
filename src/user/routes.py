from fastapi import APIRouter, Depends, status

from src.auth.deps import get_current_active_user
from src.global_deps import session_dep
from src.user import user_repo
from src.user.schemas import (
    UserEdit,
    UserChangePassword,
    UserIDB,
)

router = APIRouter(prefix="/me", tags=["Users"])


@router.get("/")
async def me(user=Depends(get_current_active_user)) -> UserIDB:
    return user


@router.patch("/edit")
async def edit(
    edit_user: UserEdit,
    user=Depends(get_current_active_user),
    session=Depends(session_dep),
) -> UserIDB:
    return await user_repo.edit_user(
        session=session,
        user=user,
        edit_user=edit_user,
    )


@router.patch("/change-password")
async def change_password(
    edit_pass: UserChangePassword,
    user=Depends(get_current_active_user),
    session=Depends(session_dep),
) -> UserIDB:
    return await user_repo.change_user_password(
        session=session, user=user, edit_pass=edit_pass
    )


@router.delete("/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_current_user(
    user=Depends(get_current_active_user),
    session=Depends(session_dep),
):
    await user_repo.delete_user(
        session=session,
        user=user,
    )
