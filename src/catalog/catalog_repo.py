from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
from sqlalchemy import select

from src.product.models import Product
from src.category.models import Category


async def get_product_by_slug(
    session: AsyncSession,
    slug: str,
) -> Product | None:
    stmt = select(Product).where(Product.slug == slug)
    result = await session.execute(stmt)
    return result.scalar_one_or_none()


async def get_category_by_slug(
    session: AsyncSession,
    slug: str,
) -> Category | None:
    stmt = (
        select(Category)
        .where(Category.slug == slug)
        .options(selectinload(Category.products))
    )
    result = await session.execute(stmt)
    return result.scalar_one_or_none()
