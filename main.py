from fastapi import FastAPI, requests
from fastapi.requests import Request

from utils.data import get_endpoints, get_images


app = FastAPI()
endpoints = get_endpoints()


@app.get("/")
def index():
    return {"endpoints": endpoints}


@app.get("/{wanted}")
async def endpoint(wanted: str, amount: int = 1, *, tags: str = None):
    print(tags)
    if wanted not in endpoints:
        return {"endpoints": endpoints}

    res = "results"
    if amount <= 1:
        res, amount = "result", 1
    elif amount > 20:
        amount = 20

    img = get_images(wanted, amount)

    return {res: img}
