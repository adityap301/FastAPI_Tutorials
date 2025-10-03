from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/", description="Returns message when root path is hit")
def get_message():
    return {"message": "Hello World!"}


@app.get("/api/{msg}", description="Echoes message sent over in the path param")
def echo_msg_path_param(msg: str):
    return {"message": msg}


@app.get("/api/", description="Echoes message sent over in the query param")
def echo_msg_path_param(msg: str):
    return {"message": msg}


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
