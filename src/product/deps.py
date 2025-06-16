from typing import Annotated

from fastapi import Depends, HTTPException, Path, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.global_deps import session_dep
from src.product.models import Product
from src.product import product_repo


async def get_product_by_id(
    product_id: Annotated[int, Path],
    session: AsyncSession = Depends(session_dep)
) -> Product:
    product = await product_repo.get_product_by_id(
        session=session,
        product_id=product_id,
    )
    if product is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return product
