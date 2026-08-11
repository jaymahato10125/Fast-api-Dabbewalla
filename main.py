from contextlib import asynccontextmanager
from fastapi import FastAPI
from database import create_tables

from routes.orders import router as orders_router
from routes.stats import router as stats_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Create database tables on startup
    create_tables()
    yield
    print("Application shutdown")


app = FastAPI(
    title="Dabbewala API",
    description="API for managing Dabbewala orders and statistics",
    version="1.0.0",
    lifespan=lifespan
)

app.include_router(orders_router)
app.include_router(stats_router)

app.get("/health", tags=["health"])
def health_check():
    return {"status": "ok"}