# Syntax
# dict_name = {key1: value, key2: value, ...}
# - Not indexed -> key/value pair
# - Changeable
# - Repeat is allowed (only values)
# - KeyError

amir_emadi = {
    "name": "Amirhossein",
    "age": 25,
    "city": "Gorgan"
}

amir_emadi["code"] = 1234

print(amir_emadi)

print(amir_emadi["name"])
# --------------------------------------------
# Nested Dictionary:
person = {
    "user1": {
    "name": "Amirhossein",
    "age": 25,
    "city": "Gorgan"
    },
    "user2": {
    "name": "Zahra",
    "age": 22,
    "city": "Gorgan"
    }
}
print(person)

print(person["user1"]["city"])
