from fastapi import FastAPI

from utils.data import get_endpoints, get_images, get_tag_list


app = FastAPI()


@app.get("/")
def index():
    return {"endpoints": get_endpoints()}


@app.get("/{endpoint}")
async def get_img(endpoint: str, amount: int = 1, *, tags: str = None):
    if endpoint not in get_endpoints():
        return {"endpoints": get_endpoints()}

    res = "results"
    if amount <= 1:
        res, amount = "result", 1
    elif amount > 20:
        amount = 20

    img = get_images(endpoint, amount, tags=tags.split() if tags else None)

    return {res: img}


@app.get("/{endpoint}/tags")
async def get_tags(endpoint: str):
    if endpoint not in get_endpoints():
        return {"endpoints": get_endpoints()}

    return {f"tags_for_{endpoint}": get_tag_list(endpoint)}
