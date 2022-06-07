import os
import yaml
from random import sample


def _open_yml(name: str) -> list[dict]:
    with open(f"./endpoints/{name}.yml", "r") as file:
        file = yaml.safe_load(file)

    return list(file.values())


def get_endpoints() -> list[str]:
    endpoints: list[str] = []
    for file in os.listdir("./endpoints"):
        if file[-4:] == ".yml":
            endpoints.append(file[:-4])

    return endpoints


def get_images(endpoint: str, amount: int, tags: list[str] = None) -> list[dict] | dict:
    file = _open_yml(endpoint)

    if tags:
        filtered_list = []
        for picture in file:
            if set(tags).issubset(picture.get("tags")):
                filtered_list.append(picture)

        if not filtered_list:
            return {"Not found": f"No image from the '{endpoint}' endpoint with tags={tags} was found!"}

        file = filtered_list

    if amount > len(file):
        amount = len(file)

    choice = sample(file, k=amount)

    if amount > 1:
        return choice
    else:
        return choice[0]


def get_tag_list(endpoint: str) -> list[str]:
    file = _open_yml(endpoint)
    tags = set()
    for img in file:
        for tag in img.get("tags"):
            tags.add(tag)

    return list(tags)
