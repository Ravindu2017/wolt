import json 
restaurant = []
counter = 0
tag = "["
file1 = open("viddsit.json", "w+")
file1.write(tag)

end = "]"
with open("restaurant.json") as json_file:
    info = json.load(json_file)
    restaurant.append(info["restaurants"])
    #for i in restaurant[0]:
        #print(i)
    for i in restaurant[0]:
        #counter += 1
        start = "{\"model\": \"wolt.restaurant\", \"pk\": "+str(counter) +" , \"fields\": "
        content = start + str(restaurant[0][counter])+"}, "
        print(content)
        counter += 1
        #with open("places.json") as p:
        file1.write(content)


#with open("places.json") as b:
file1.write(end)
file1.close()

        #if counter == 3:
            #break
"""
place = str(restaurant[0][0])
#print(restaurant[0][0])
#content = "[","{\"pk\":1,\"model\": \"wolt.restaurant\" ",(restaurant[0][0]),"}","]"
content = "[{\"pk\":1,\"model\": \"wolt.restaurant\", \"fields\": "+place+"}]"
start = "[{\"pk\":1,\"model\": \"wolt.restaurant\", \"fields\": "
end = "}]"
#start = "[{\"pk\":{},\"model\": \"wolt.restaurant\", \"fields\": ".format(i)
#print("[","{",restaurant[0][0],"}","]")
#print(content)
counter = 0
for i in range(0,10):
    counter += 1
    number = "number {}".format(counter)
    start = "[{\"pk\": "+str(counter) +" ,\"model\": \"wolt.restaurant\", \"fields\": "#.format(counter)
    print(start)"""

