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


@router.post("/categories/{category_slug}/{product_slug}")
async def add_product_in_cart(
    slug: str,
    user: User = Depends(get_current_active_user),
    session=Depends(session_dep),
) -> CartIDB:
    cart = await cart_repo.add_product_to_cart(
        session=session,
        product_slug=slug,
        user=user,
    )
    return cart


@router.delete("/categories/{category_slug}/{product_slug}")
async def remove_product_from_cart(
    slug: str,
    user: User = Depends(get_current_active_user),
    session=Depends(session_dep),
) -> CartIDB:
    cart = await cart_repo.remove_product(
        session=session,
        user=user,
        product_slug=slug,
    )
    return cart


@router.delete("/cart")
async def clear_cart(
    session=Depends(session_dep),
    user: User = Depends(get_current_active_user),
) -> CartIDB:
    cart = await cart_repo.clear_user_cart(
        session=session,
        user=user,
    )
    return cart
