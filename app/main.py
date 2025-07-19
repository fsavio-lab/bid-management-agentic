from fastapi import FastAPI
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware
from app.db.stores import MONGO_STORE
from app.api import router as api_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    MONGO_STORE.connect()
    yield
    MONGO_STORE.disconnect()


app = FastAPI(lifespan=lifespan)

app.add_middleware(CORSMiddleware, ALLOWED_HOSTS=[])

app.include_router(api_router)
