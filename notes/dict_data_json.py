## Converting dictionary data to json data and storing it in a file
import json

some_dict = {
    "name": "Example",
    "colour": "Blue",
    "height": 50,
    "is_happy": False
}

json_string = json.dumps(some_dict)

print(some_dict)
print(json_string)

## Take the json string and write it to a file

#with open ("json_data_example.json", 'w') as f:
    #json.dump(some_dict, f)

## Read data from json file

with open("json_data_example.json", "r") as f:
    data = json.load(f)

#print(data)
#print(type(data))
#print(data["name"])

## Changing data and writing it to the file
data["name"] = "Blah"

with open("json_data_example.json", "w") as f:
    # convert JSON to Python Dictionary
    json.dump(data, f)