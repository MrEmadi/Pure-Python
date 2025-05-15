# max(__iterable):
# __iterable -> numeric sequence (list, tuple, set, dict) - TypeError
# return type -> int

numbers = [12, -9, 0, 44, 1, 13, -7, 25] # :list

print(f"Max of {numbers} = {max(numbers)}")
# ---------------------------------------------
# max(*args):
# *args -> int
# return type -> int

print(f"Max of [12, -9, 0, 25] = {max(12, -9, 0, 25)}")
