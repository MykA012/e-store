from fastapi import APIRouter

router = APIRouter(prefix="/products")


@router.get("/")
async def foo(): ...