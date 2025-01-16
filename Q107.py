import json

data = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

with open("data.json", "w") as file:
    json.dump(data, file)

with open("data.json", "r") as file:
    loaded_data = json.load(file)

loaded_data["age"] = 31

with open("data.json", "w") as file:
    json.dump(loaded_data, file)

print("Updated JSON data written to file.")
