from models import Example

import json

restaurant = []
counter = 0
tag = "["

with open("restaurants.json") as json_file:
    info = json.load(json_file)
    for i in info["restaurants"]:
        test = Example()
        test.name = i["name"]
        test.description = i["description"]
        test.online = i["online"]
        test.save()
