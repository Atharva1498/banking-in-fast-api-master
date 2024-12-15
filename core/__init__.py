from fastapi import FastAPI
from shared.db import init_db, close_db

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    """Initialize the database on application startup."""
    await init_db()

@app.on_event("shutdown")
async def shutdown_event():
    """Close the database connection on application shutdown."""
    await close_db()

# Example health check route
@app.get("/")
async def root():
    return {"message": "API is working with Tortoise-ORM!"}
