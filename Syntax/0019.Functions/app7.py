# Parameters with default values:

def users_message(name: str, age: int, year = 2000) -> None:
    print(f'{year} -> {name}: {age} years old.')

users_message(name="John", age=36, year=2020)

users_message(name="Amirhossein", age=25)
