# Heads or Tails? Create a coin flip program:

import random

random_number = random.randint(1, 2)
message = "Heads"
if random_number == 2: message = "Tails"
print(f"Coin Flip: {message}")
