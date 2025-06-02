from datetime import datetime
from random import randrange

class User:
    def __init__(self, name: str, birthyear: int):
        self.id = randrange(1, 100000)
        self.name = name
        self.birthyear = birthyear
    # Define a method:
    def age_calc(self) -> int:
        return datetime.now().year - self.birthyear

new_user_1 = User(name='Amirhossein', birthyear=2000)
new_user_2 = User(name='Zahra', birthyear=2002)
print(f'{new_user_1.name} is {new_user_1.age_calc()} years old.')
print(f'{new_user_2.name} is {new_user_2.age_calc()} years old.')
