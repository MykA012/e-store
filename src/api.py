from fastapi import APIRouter

from src.auth.routes import router as auth_router
from src.catalog.routes import router as catalog_router
from src.cart.routes import router as cart_router
from src.user.routes import router as user_router
from src.product.routes import router as product_router
from src.category.routes import router as category_router
from src.order.routes import router as order_router

root_router = APIRouter()

root_router.include_router(router=auth_router)
root_router.include_router(router=catalog_router)
root_router.include_router(router=cart_router)
root_router.include_router(router=user_router)
root_router.include_router(router=product_router)
root_router.include_router(router=category_router)
root_router.include_router(router=order_router)
