from fastapi import APIRouter, Depends, HTTPException, status

from src.global_deps import session_dep
from src.category.deps import get_category_by_slug
from src.product.product_repo import get_product_in_category
from src.product.schemas import ProductIDB
from src.category.schemas import CategoryIDB
from src.category.category_repo import all_categories
from src.category.schemas import CategoryWithProducts


router = APIRouter(tags=["Catalog"])


@router.get("/categories")
async def get_categories(
    session=Depends(session_dep),
) -> list[CategoryIDB]:
    return await all_categories(session)


@router.get("/categories/{category_slug}")
async def get_category_with_products(
    category_with_products=Depends(get_category_by_slug),
) -> CategoryWithProducts:
    return category_with_products


@router.get("/categories/{category_slug}/{product_slug}")
async def get_category_product(
    category_slug: str,
    product_slug: str,
    session=Depends(session_dep),
) -> ProductIDB:
    product = await get_product_in_category(
        session=session,
        category_slug=category_slug,
        product_slug=product_slug,
    )
    if product is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return product
