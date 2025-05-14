# Figure out how to pick a random name from a list of names:

# First Option:
import random

names = ["Ali", "Zahra", "Mehdi", "Amirhossein", "Amin", "Zeynab", "Maryam",
         "Azar", "Nader", "Sara"]
print(f"Random Name: {names[random.randrange(0, len(names))]}")
