from fastapi import APIRouter, Depends, status

from src.global_deps import session_dep
from src.product.deps import get_product_by_id
from src.product import product_repo
from src.product.schemas import (
    ProductIDB,
    ProductCreate,
    ProductPatch,
    ProductPut,
)

router = APIRouter(prefix="/products", tags=["Products"])


@router.get("/")
async def get_all_products(session=Depends(session_dep)) -> list[ProductIDB]:
    products = await product_repo.all_products(session)
    return products


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_product(
    product_in: ProductCreate,
    session=Depends(session_dep),
) -> ProductIDB:
    product = await product_repo.add_product(
        session=session,
        product_in=product_in,
    )
    return product


@router.get("/{product_id}")
async def get_product(product=Depends(get_product_by_id)) -> ProductIDB:
    return product


@router.patch("/{product_id}")
async def patch_product(
    product_update: ProductPatch,
    product=Depends(get_product_by_id),
    session=Depends(session_dep),
) -> ProductIDB:
    return await product_repo.update_product(
        session=session,
        product=product,
        product_update=product_update,
        partial=True,
    )


@router.put("/{product_id}")
async def put_product(
    product_update: ProductPut,
    product=Depends(get_product_by_id),
    session=Depends(session_dep),
) -> ProductIDB:
    return await product_repo.update_product(
        session=session,
        product=product,
        product_update=product_update,
        partial=False,
    )


@router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_product(
    product=Depends(get_product_by_id),
    session=Depends(session_dep),
) -> None:
    await product_repo.delete_product(
        session=session,
        product=product
    )
