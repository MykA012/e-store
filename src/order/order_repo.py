from datetime import datetime, timedelta
from uuid import UUID, uuid4

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
from sqlalchemy import select

from src.cart import cart_repo
from src.order.models import Order
from src.user.models import User
from src.cart.models import Item


async def get_users_orderlist(
    session: AsyncSession,
    user: User,
) -> list[Order]:
    stmt = select(Order).where(Order.user_id == user.id)
    result = await session.execute(stmt)
    orderlist = result.scalars().all()
    return orderlist


async def get_users_order(
    session: AsyncSession,
    user: User,
    tracking_id: UUID,
) -> Order:
    stmt = (
        select(Order)
        .where((Order.tracking_id == tracking_id) & (Order.user_id == user.id))
        .options(
            selectinload(Order.items).joinedload(Item.product),
            selectinload(Order.payment),
        )
    )
    result = await session.execute(stmt)
    order = result.scalar_one_or_none()
    return order


async def place_order(
    session: AsyncSession,
    delivery_address: str,
    user: User,
):
    cart = await cart_repo.get_user_cart(
        session=session,
        user=user,
    )

    order = Order(
        user_id=user.id,
        tracking_id=uuid4(),
        total_price=cart.total_price,
        delivery_address=delivery_address,
        delivery_date=datetime.now() + timedelta(days=7),
        items=[item for item in cart.items],
    )
    session.add(order)
    await session.commit()
    await session.refresh(order)
    return order
