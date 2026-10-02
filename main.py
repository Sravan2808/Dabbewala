from contextlib import asynccontextmanager
from fastapi import FastAPI
from database import create_tables

from routes.orders import router as orders_router
from routes.stats import router as stats_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_tables()
    print("Tables created successfully.")
    yield
    print("Application shutdown.")



app = FastAPI(title="Dabbe Wala Management API",
              description="A simple API for managing orders in the Dabbe Wala system.",
              lifespan=lifespan, version="1.0.0")


app.include_router(orders_router)
app.include_router(stats_router)

