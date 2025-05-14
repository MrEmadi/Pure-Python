# random.choice(seq):
# random -> class name
# seq -> Sequence (list, tuple, set, str, dict)

import random

names = ["Ali", "Zahra", "Mehdi", "Amirhossein", "Amin", "Zeynab", "Maryam",
         "Azar", "Nader", "Sara"]

print(f"Random Name: {random.choice(names)}") # :list
print(f"Random Letter: {random.choice('Amirhossein')}") # :str
