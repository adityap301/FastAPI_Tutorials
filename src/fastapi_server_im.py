from fastapi import FastAPI
from routers import product_router_im


app = FastAPI()


@app.get("/", description="Returns message when root path is hit")
def get_message():
    return {"message": "Hello World!"}


app.include_router(product_router_im.router)
