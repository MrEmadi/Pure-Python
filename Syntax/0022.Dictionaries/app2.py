amir_emadi = {
    "name": "Amirhossein",
    "age": 25,
    "city": "Gorgan"
}

# Loop through by keys:
for key in amir_emadi: print(f"[{key}] -> {amir_emadi[key]}")

# Loop through by items():
for key, value in amir_emadi.items(): print(f"{key} -> {value}")
