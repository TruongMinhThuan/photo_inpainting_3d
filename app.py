from typing import Union

from fastapi import FastAPI
import os

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/generate-3Dphoto")
def generate_3Dphoto():
    command = "python main.py --config argument.yml"
    os.system(command)

    return {"data":1}
