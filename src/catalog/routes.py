from fastapi import APIRouter, Depends, HTTPException, status

from src.global_deps import session_dep
from src.product.schemas import ProductIDB
from src.category.schemas import CategoryIDB
from src.category.category_repo import all_categories
from src.catalog.schemas import CategoryWithProducts
from src.catalog import catalog_repo


router = APIRouter(tags=["Catalog"])


@router.get("/product/{product_slug}")
async def get_product_by_slug(
    product_slug: str,
    session=Depends(session_dep),
) -> ProductIDB:
    product = await catalog_repo.get_product_by_slug(
        session=session,
        slug=product_slug,
    )
    if product is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return product


@router.get("/catalog/")
async def get_categories(
    session=Depends(session_dep),
) -> list[CategoryIDB]:
    return await all_categories(session)


@router.get("/category/{category_slug}")
async def get_category_products(
    category_slug: str,
    session=Depends(session_dep),
) -> CategoryWithProducts:
    category = await catalog_repo.get_category_by_slug(
        session=session,
        slug=category_slug,
    )
    if category is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return category
