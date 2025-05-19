def greet():
    print("Hi there!")
    print("My name is Amirhossein!")
    print("Welcome to my App!")

greet()
print("-" * 25)
greet()
# -----------------------------------
# Function with Parameter:
def greet_with_name(name: str):
    print(f"Hi, {name}!")
    print("My name is Amirhossein!")
    print("Welcome to my App!")

# Function with Argument:
greet_with_name("Zahra")
