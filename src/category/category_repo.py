from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from src.category.models import Category
from src.category.schemas import (
    CategoryCreate,
    CategoryPatch,
    CategoryPut,
)


async def all_categories(session: AsyncSession) -> list[Category]:
    stmt = select(Category)
    result = await session.execute(stmt)
    return list(result.scalars().all())


async def add_category(
    session: AsyncSession,
    category_in: CategoryCreate,
) -> Category:
    new_category = Category(**category_in.model_dump())
    session.add(new_category)
    await session.commit()
    await session.refresh(new_category)

    return new_category


async def get_category_by_id(
    session: AsyncSession, category_id: int
) -> Category | None:
    return await session.get(Category, category_id)


async def update_category(
    session: AsyncSession,
    category: Category,
    category_update: CategoryPatch | CategoryPut,
    partial: bool = False,
) -> Category:
    for name, value in category_update.model_dump(exclude_unset=partial).items():
        setattr(category, name, value)

    await session.commit()
    await session.refresh(category)
    return category


async def delete_category(session: AsyncSession, category: Category) -> None:
    session.delete(category)
    await session.commit()
