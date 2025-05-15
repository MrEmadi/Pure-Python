# for loop Syntax

# for <variable_name> in range(a, b):
#   ...
# range(a, b) -> [a, b)

for number in range(0, 12): print(number)
# -------------------------------------------
family = ['Zahra', 'Amir', 'Bagher', 'Narges']
for name in range(len(family)): print(f"{name} -> {family[name]}")
# -------------------------------------------
for name in range(0, len(family), 3): print(f"[{name}] -> {family[name]}")
