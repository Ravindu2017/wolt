import json

restaurant = []
counter = 0
tag = "["

with open("restaurants.json") as json_file:
    info = json.load(json_file)
    for i in info["restaurants"]:
        print(i["description"])

##end = "]"
##with open("restaurants.json") as json_file:
##    info = json.load(json_file)
##    restaurant.append(info["restaurants"])
##    #for i in restaurant[0]:
##        #print(i)
##    for i in restaurant[0]:
##        #counter += 1
##        start = "{\"model\": \"wolt.restaurant\", \"pk\": "+str(counter+1) +" , \"fields\": "
##        content = start + str(restaurant[0][counter])+"}, "
##        print(content)
##        if "ö" in content:
##            print("\\u")
##            #content.replace("\\", "\\\\")
##            content.replace("\\", "butt")
##        #print(content)
##        counter += 1
##        if counter > 3:
##            break
##        


