# Positional vs Keyword Arguments:

def greet_with(name: str, location: str):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")

# Positional Arguments:
greet_with("Amirhossein", "Gorgan")

# Keyword Arguments:
greet_with(location="Tehran", name="Zahra")
