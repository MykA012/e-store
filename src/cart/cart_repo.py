from sqlalchemy.ext.asyncio import AsyncSession

from src.user.models import User
from src.cart.models import Cart


async def create_cart(session: AsyncSession, user: User) -> Cart:
    cart = Cart(user_id=user.id)
    session.add(cart)
    await session.commit()
    await session.refresh(cart)
    return cart


async def add_product_to_cart(
    session: AsyncSession,
    user: User,
    slug: str,
    quantity: int = 1,
):
    product = ...
