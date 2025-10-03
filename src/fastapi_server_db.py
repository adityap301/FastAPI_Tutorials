from fastapi import FastAPI, Depends
from routers import product_router_db
from database.db_models.base import Base
from database.db_connection import create_db_and_tables, get_db_conn


app = FastAPI()


def init_db():
    create_db_and_tables()


@app.on_event("startup")
def on_startup():
    init_db()


@app.get("/", description="Returns message when root path is hit")
def get_message():
    return {"message": "Hello World!"}

app.include_router(product_router_db.router)
