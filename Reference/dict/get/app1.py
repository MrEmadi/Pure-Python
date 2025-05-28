# dict.get(key, __default):
# dict -> 'dict' data type
# key -> T (str, int, ...)
# __default = None -> T (str, int, ...)
# return type -> ValueT (int, str, ...)
# not found -> __default

my_dict = {
    "name": "Amirhossein Emadi",
    "age": 25,
    "city": "Gorgan",
    "is_male": True,
    "hobbies": ['football', 'ping-pong', 'study', 'programming']
}

print(my_dict.get("city"))

print(my_dict.get("code"))

print(my_dict.get("code", "Unknown!"))
