# Đọc ghi file JSON 

import json

user = {
    "name": "Dung",
    "age": 22
}

with open("user.json", "w") as file:
    json.dump(user, file, indent=2)

with open("user.json", "r") as file:
    data = json.load(file)

print(data)