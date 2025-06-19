from decimal import Decimal

from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
from sqlalchemy import select, delete

from src.product import product_repo
from src.user.models import User
from src.cart.models import Cart, Item


async def create_user_cart(session: AsyncSession, user: User) -> Cart:
    cart = Cart(user_id=user.id)
    session.add(cart)
    await session.commit()
    await session.refresh(cart)
    return cart


async def get_user_cart(
    session: AsyncSession,
    user: User,
) -> Cart:
    stmt = (
        select(Cart)
        .where(Cart.user_id == user.id)
        .options(selectinload(Cart.items).selectinload(Item.product))
    )
    result = await session.execute(stmt)
    cart = result.scalar_one()
    cart.items_count = sum(item.quantity for item in cart.items)
    cart.total_price = sum(item.quantity * item.product.price for item in cart.items)
    await session.commit()
    await session.refresh(cart)
    return cart


async def clear_user_cart(
    session: AsyncSession,
    user: User,
) -> Cart:
    stmt = (
        select(Cart)
        .where(Cart.user_id == user.id)
        .options(selectinload(Cart.items))
    )
    result = await session.execute(stmt)
    cart = result.scalar_one()

    await session.execute(delete(Item).where(Item.cart_id == cart.id))

    cart.items_count = 0
    cart.total_price = Decimal("0")

    await session.commit()
    await session.refresh(cart)
    return cart


async def add_product_to_cart(
    session: AsyncSession,
    user: User,
    product_slug: str,
    quantity: int = 1,
) -> Cart:
    product = await product_repo.get_product_by_slug(
        session=session,
        product_slug=product_slug,
    )
    if product is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    stmt = (
        select(Cart)
        .where(Cart.user_id == user.id)
        .options(selectinload(Cart.items).selectinload(Item.product))
    )
    result = await session.execute(stmt)
    cart = result.scalar_one_or_none()

    existing_item = next(
        (item for item in cart.items if item.product_id == product.id), None
    )
    if existing_item:
        existing_item.quantity += quantity
    else:
        new_item = Item(
            quantity=quantity,
            cart_id=cart.id,
            product_id=product.id,
        )
        session.add(new_item)
        cart.items.append(new_item)
        await session.flush()

    cart.items_count = sum(item.quantity for item in cart.items)
    cart.total_price = sum(item.quantity * item.product.price for item in cart.items)
    await session.commit()
    await session.refresh(cart)
    return cart
