from decimal import Decimal
from datetime import datetime, timedelta
from uuid import UUID, uuid4

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
from sqlalchemy import select

from src.cart import cart_repo
from src.order.models import Order, PaymentMethod
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
        )
    )
    result = await session.execute(stmt)
    order = result.scalar_one_or_none()
    return order


async def create_order(
    session: AsyncSession,
    payment: PaymentMethod,
    delivery_address: str,
    user: User,
):
    cart = await cart_repo.get_user_cart(
        session=session,
        user=user,
    )

    order = Order(
        tracking_id=uuid4(),
        total_price=cart.total_price,
        payment_method=payment,
        delivery_address=delivery_address,
        delivery_date=datetime.now() + timedelta(days=7),
        user_id=user.id,
    )
    session.add(order)
    await session.flush()

    for item in cart.items:
        item.cart_id = None
        item.order_id = order.id

    cart.total_price = Decimal("0")
    cart.items_count = 0

    await session.commit()
    await session.refresh(order)

    stmt = select(Order).where(Order.id == order.id).options(selectinload(Order.items))
    result = await session.execute(stmt)
    order = result.scalar_one()

    return order


async def delete_order(
    session: AsyncSession,
    order: Order,
) -> None:
    await session.delete(order)
    await session.commit()
