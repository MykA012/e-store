from fastapi import APIRouter, Depends

from src.auth.service import get_current_active_user
from src.global_deps import session_dep
from src.user.models import User


router = APIRouter(tags=["Cart"])


@router.get("/cart")
async def my_cart(
    user: User = Depends(get_current_active_user),
    session=Depends(session_dep),
): ...


@router.post("/{slug}")
async def add_product_in_cart(
    slug: str,
    user: User = Depends(get_current_active_user),
    session=Depends(session_dep),
):
    ...