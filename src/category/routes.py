from fastapi import APIRouter, Depends, status

from src.global_deps import session_dep
from src.auth.deps import get_current_admin
from src.category.deps import get_category_by_id
from src.category import category_repo
from src.category.schemas import (
    CategoryIDB,
    CategoryCreate,
    CategoryPatch,
    CategoryPut,
)

router = APIRouter(prefix="/admin/categories", tags=["Admin"])


@router.get("/")
async def get_all_categories(
    session=Depends(session_dep),
    admin=Depends(get_current_admin),
) -> list[CategoryIDB]:
    categories = await category_repo.all_categories(session)
    return categories


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_category(
    category_in: CategoryCreate,
    session=Depends(session_dep),
    admin=Depends(get_current_admin),
) -> CategoryIDB:
    category = await category_repo.add_category(
        session=session,
        category_in=category_in,
    )
    return category


@router.get("/{category_id}")
async def get_category(
    category=Depends(get_category_by_id),
    admin=Depends(get_current_admin),
) -> CategoryIDB:
    return category


@router.patch("/{category_id}")
async def patch_category(
    category_update: CategoryPatch,
    category=Depends(get_category_by_id),
    session=Depends(session_dep),
    admin=Depends(get_current_admin),
) -> CategoryIDB:
    return await category_repo.update_category(
        session=session,
        category=category,
        category_update=category_update,
        partial=True,
    )


@router.put("/{category_id}")
async def put_category(
    category_update: CategoryPut,
    category=Depends(get_category_by_id),
    session=Depends(session_dep),
    admin=Depends(get_current_admin),
) -> CategoryIDB:
    return await category_repo.update_category(
        session=session,
        category=category,
        category_update=category_update,
        partial=False,
    )


@router.delete("/{category_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_category(
    category=Depends(get_category_by_id),
    session=Depends(session_dep),
    admin=Depends(get_current_admin),
) -> None:
    await category_repo.delete_category(
        session=session,
        category=category,
    )
