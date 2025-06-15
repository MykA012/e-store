from fastapi import APIRouter

router = APIRouter(prefix="/categories", tags=["Categories"])


@router.get("/")
async def get_all_categories(): ...


@router.post("/")
async def create_category(): ...


@router.get("/{category_id}")
async def get_category(category_id: int): ...


@router.patch("/{category_id}")
async def patch_category(category_id: int): ...


@router.put("/{category_id}")
async def put_category(category_id: int): ...


@router.delete("/{category_id}")
async def delete_category(category_id: int): ...
