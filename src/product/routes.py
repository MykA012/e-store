from fastapi import APIRouter

from src.product.schemas import (
    ProductIDB,
    ProductCreate,
    ProductPatch,
    ProductPut,
)

router = APIRouter(prefix="/products", tags=["Products"])


@router.get("/")
async def get_all_products() -> list[ProductIDB]: ...


@router.post("/")
async def create_product(product_in: ProductCreate) -> ProductIDB: ...


@router.get("/{product_id}")
async def get_product(product_id: int) -> ProductIDB: ...


@router.patch("/{product_id}")
async def patch_product(product_id: int, product_in: ProductPatch) -> ProductIDB: ...


@router.put("/{product_id}")
async def put_product(product_id: int, product_in: ProductPut) -> ProductIDB: ...


@router.delete("/{product_id}")
async def delete_product(product_id: int) -> ProductIDB: ...
