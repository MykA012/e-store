from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status

from src.auth.deps import get_current_active_user
from src.global_deps import session_dep
from src.user.models import User
from src.order import order_repo
from src.order.schemas import (
    OrderIDB,
    OrderWithItem,
)


router = APIRouter()


@router.get("/orderlist")
async def get_orderlist(
    user: User = Depends(get_current_active_user),
    session=Depends(session_dep),
) -> list[OrderIDB]:
    orderlist = await order_repo.get_users_orderlist(
        session=session,
        user=user,
    )
    return orderlist


@router.get("/orderlist")
async def get_order(
    order: UUID,
    user: User = Depends(get_current_active_user),
    session=Depends(session_dep),
) -> OrderWithItem:
    order = await order_repo.get_users_order(
        session=session,
        user=user,
        tracking_id=order,
    )
    if order is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return order


@router.post("/cart", status_code=status.HTTP_201_CREATED)
async def place_an_order(
    delivery_address: str,
    user: User = Depends(get_current_active_user),
    session=Depends(session_dep),
):
    ...