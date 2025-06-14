import uvicorn
from fastapi import FastAPI

from src.database.core import init_db
from src.api import root_router

app = FastAPI(lifespan=init_db)
app.include_router(router=root_router)


if __name__ == "__main__":
    uvicorn.run("src.main:app", reload=True)
