from fastapi import APIRouter, Depends

from src.auth.deps import get_current_active_user
from src.cart import cart_repo
from src.global_deps import session_dep
from src.user.models import User
from src.cart.schemas import CartIDB


router = APIRouter(tags=["Cart"])


@router.get("/cart")
async def my_cart(
    session=Depends(session_dep),
    user: User = Depends(get_current_active_user),
) -> CartIDB:
    cart = await cart_repo.get_user_cart(
        session=session,
        user=user,
    )
    return cart


@router.post("/{slug}")
async def add_product_in_cart(
    slug: str,
    user: User = Depends(get_current_active_user),
    session=Depends(session_dep),
) -> dict:
    await cart_repo.add_product_to_cart(
        session=session,
        product_slug=slug,
        user=user,
    )
    return {"status": "ok"}
