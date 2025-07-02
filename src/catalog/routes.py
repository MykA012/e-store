from fastapi import APIRouter, Depends, HTTPException, status

from src.global_deps import session_dep
from src.category.deps import get_category_by_slug, get_category_with_products
from src.product.schemas import ProductIDB
from src.category.schemas import CategoryIDB
from src.category.category_repo import all_categories
from src.category.schemas import CategoryWithProducts
from src.catalog import catalog_repo


router = APIRouter(tags=["Catalog"])


@router.get("/categories")
async def get_categories(
    session=Depends(session_dep),
) -> list[CategoryIDB]:
    return await all_categories(session)


@router.get("/categories/{category_slug}")
async def get_category(
    category=Depends(get_category_by_slug),
    session=Depends(session_dep),
) -> CategoryIDB:
    if category is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return category


@router.get("/categories/{category_slug}/products")
async def get_category(
    category=Depends(get_category_with_products),
    session=Depends(session_dep),
) -> CategoryWithProducts:
    if category is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return category


@router.get("/categories/{category_slug}/products/{product_slug}")
async def get_category_products(): ...


# @router.get("/categories/{category_slug}")


# @router.get("/products/{product_slug}")
# async def get_product_by_slug(
#     product_slug: str,
#     session=Depends(session_dep),
# ) -> ProductIDB:
#     product = await catalog_repo.get_product_by_slug(
#         session=session,
#         slug=product_slug,
#     )
#     if product is None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
#     return product
