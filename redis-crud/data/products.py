import json

with open("data/products.json", "r") as file:
    data = json.loads(file.read())
