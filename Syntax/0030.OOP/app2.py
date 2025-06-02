# Define a class
# -> with 'class' keyword
# -> class name: Pascal case

import random

class User:
    # Constructor (__init__ function):
    def __init__(self, name: str, age: int):
        # Attributes:
        self.id = random.randrange(1, 100000) # initialise attribute
        self.name = name  # by user
        self.age = age    # by user

# Define an object:
new_user_1 = User(name='Amirhossein', age=25)
new_user_2 = User(name='Zahra', age=23)
print(f'{new_user_1.name} is {new_user_1.age} years old.')
print(f'{new_user_2.name} is {new_user_2.age} years old.')
