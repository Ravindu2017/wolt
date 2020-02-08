from menu.models import Restaurants, Coordinate, Trendy

import json

with open("menu\\fixtures\\restaurants.json") as json_file:
    info = json.load(json_file)
    for i in info["restaurants"]:
        tags = Trendy()
        place = Restaurants()
        location = Coordinate()
        place.blurhash = i["blurhash"]
        place.city = i["city"]
        place.currency = i["currency"]
        place.delivery_price = float(i["delivery_price"])/100
        place.description = i["description"]
        place.image = i["image"]
        place.name = i["name"]
        place.online = i["online"]
        location.latitude = i["location"][0]
        location.longitude = i["location"][1]
        location.save()
        place.location = location
        place.tags = tags
        if i["tags"]:
            tags.tag_1 = i["tags"][0]
            tags.tag_2 = i["tags"][1]            
        else:
            tags.tag_1 = ""
            tags.tag_2 = ""
        tags.save()
        place.location = location
        place.tags = tags
        place.save()
        
        
        
