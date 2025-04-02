from fastapi import FastAPI
from app.routes import router

app = FastAPI(
    title="Predictive Model API",
    description="An API that exposes a simple predictive model.",
)

app.include_router(router)