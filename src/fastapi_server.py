from fastapi import FastAPI
import uvicorn
from routers import product_router_im


app = FastAPI()

@app.get("/", description="Root path")
def read_root():
    return {"message": "Hello World!"}


app.include_router(product_router_im.router)


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000, reload=True)
