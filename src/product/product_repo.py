from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from src.product.models import Product
from src.category.models import Category
from src.product.schemas import (
    ProductCreate,
    ProductPatch,
    ProductPut,
)


async def all_products(session: AsyncSession) -> list[Product]:
    stmt = select(Product)
    result = await session.execute(stmt)
    return list(result.scalars().all())


async def add_product(
    session: AsyncSession,
    product_in: ProductCreate,
) -> Product:
    new_product = Product(**product_in.model_dump())
    session.add(new_product)
    await session.commit()
    await session.refresh(new_product)

    return new_product


async def get_product_by_id(
    session: AsyncSession,
    product_id: int,
) -> Product | None:
    return await session.get(Product, product_id)


async def get_product_by_slug(
    session: AsyncSession,
    product_slug: str,
) -> Product | None:
    stmt = select(Product).where(Product.slug == product_slug)
    result = await session.execute(stmt)
    return result.scalar_one_or_none()


async def get_product_in_category(
    session: AsyncSession,
    category_slug: str,
    product_slug: str,
) -> Product | None:
    stmt = (
        select(Product)
        .join(Product.category)
        .where(
            Product.slug == product_slug,
            Category.slug == category_slug,
        )
    )
    result = await session.execute(stmt)
    return result.scalar_one_or_none()


async def update_product(
    session: AsyncSession,
    product: Product,
    product_update: ProductPatch | ProductPut,
    partial: bool = False,
) -> Product:
    for name, value in product_update.model_dump(exclude_unset=partial).items():
        setattr(product, name, value)

    await session.commit()
    await session.refresh(product)
    return product


async def delete_product(session: AsyncSession, product: Product) -> None:
    await session.delete(product)
    await session.commit()
