from uuid import UUID

from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status,
    Body,
)

from src.auth.deps import get_current_active_user
from src.global_deps import session_dep
from src.user.models import User
from src.order.models import PaymentMethod
from src.order import order_repo
from src.order.schemas import (
    OrderIDB,
    OrderWithItems,
)


router = APIRouter(tags=["Order"])


@router.get("/orderlist")
async def get_order(
    order: UUID | None = None,
    user: User = Depends(get_current_active_user),
    session=Depends(session_dep),
) -> list[OrderIDB] | OrderWithItems:
    if order is None:
        orderlist = await order_repo.get_users_orderlist(
            session=session,
            user=user,
        )
    else:
        orderlist = await order_repo.get_users_order(
            session=session,
            user=user,
            tracking_id=order,
        )
    if orderlist is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return orderlist


@router.post("/cart", status_code=status.HTTP_201_CREATED)
async def place_an_order(
    payment: PaymentMethod,
    delivery_address: str = Body(),
    user: User = Depends(get_current_active_user),
    session=Depends(session_dep),
) -> OrderWithItems:
    order = await order_repo.create_order(
        session=session,
        payment=payment,
        delivery_address=delivery_address,
        user=user,
    )
    return order
