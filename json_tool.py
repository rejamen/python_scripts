"""Some json files usefull operations."""
import json


data = {
    "people": {
        "name": "Reinaldo J.",
        "last_name": "Menendez",
        "age": 31
    }
}

with open('data_file.json', 'w') as write_file:
    json.dump(data, write_file, indent=4)

json_str = json.dumps(data, write_file, indent=4)
print(json_str)
write_file.close()

with open('data_file.json', 'r') as read_file:
    data = json.load(read_file)
    print(type(data))
    print(data['people']['name'])

data_str = json.loads(json_str)
print(data_str)
