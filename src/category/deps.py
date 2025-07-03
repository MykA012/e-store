from typing import Annotated

from fastapi import Depends, HTTPException, Path, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.global_deps import session_dep
from src.category.models import Category
from src.category import category_repo


async def get_category_by_id(
    category_id: Annotated[int, Path], session: AsyncSession = Depends(session_dep)
) -> Category:
    category = await category_repo.get_category_by_id(
        session=session,
        category_id=category_id,
    )
    if category is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return category


async def get_category_by_slug(
    category_slug: Annotated[str, Path], session: AsyncSession = Depends(session_dep)
) -> Category:
    category = await category_repo.get_category_with_products(
        session=session,
        slug=category_slug,
    )
    if category is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return category
