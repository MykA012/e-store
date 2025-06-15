from fastapi import APIRouter

router = APIRouter(prefix="/products", tags=["Products"])


@router.get("/")
async def get_all_products(): ...


@router.post("/")
async def create_product(): ...


@router.get("/{product_id}")
async def get_product(product_id: int): ...


@router.patch("/{product_id}")
async def patch_product(product_id: int): ...


@router.put("/{product_id}")
async def put_product(product_id: int): ...


@router.delete("/{product_id}")
async def delete_product(product_id: int): ...
