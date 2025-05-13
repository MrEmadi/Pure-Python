import random

print(random.random()) # float: [0, 1)

print(random.random() * 10) # float: [0, 10)
# --------------------------------
print(random.randint(10, 1000)) # int: [a, b]
# --------------------------------
print(random.randrange(10, 12)) # int: [a, b)
# --------------------------------
