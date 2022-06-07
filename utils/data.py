import os
import yaml
from random import sample


def get_endpoints() -> list[str]:
    endpoints: list[str] = []
    for file in os.listdir("./endpoints"):
        if file[-4:] == ".yml":
            endpoints.append(file[:-4])

    return endpoints


def get_images(endpoint: str, amount: int, tags: list[str] = None) -> list[dict] | dict:
    with open(f"./endpoints/{endpoint}.yml", "r") as file:
        yml_file = yaml.safe_load(file)

    if amount > len(yml_file):
        amount = len(yml_file)

    choice = sample(list(yml_file.values()), k=amount)

    if amount > 1:
        return choice
    else:
        return choice[0]
