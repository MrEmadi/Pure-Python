# dict.items():
# dict -> 'dict' data type
# return type -> object (dict_items[key, value])

my_dict = {
    "name": "Amirhossein Emadi",
    "age": 25,
    "city": "Gorgan",
    "is_male": True,
    "hobbies": ['football', 'ping-pong', 'study', 'programming']
}

for key, value in my_dict.items(): print(key, " -> ", value)
