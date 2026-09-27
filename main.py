# main.py

from contextlib import asynccontextmanager
from fastapi import FastAPI
from engine import create_tables
from routes.review_routes import router as review_router


# control you starting and ending of server
@asynccontextmanager
async def lifespan(params : FastAPI):
    print("✅ Server has been started.")
    create_tables()
    yield
    print("❌ Server has been stopped.")


app = FastAPI(
    title = "Theater App Backend",
    description = "Backend Api of reviews of Theater App",
    lifespan = lifespan
)

app.include_router(review_router)

"localhost:8000"
@app.get("/")
def hello():
    return {"message": "Hello I am here."}