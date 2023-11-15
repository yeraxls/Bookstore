from fastapi import FastAPI
from src.routers.books_router import router
app = FastAPI()

app.include_router(router)