# min(__iterable):
# __iterable -> numeric sequence (list, tuple, set, dict) - TypeError
# return type -> int

numbers = [12, -9, 0, 44, 1, 13, -7, 25] # :list

print(f"Max of {numbers} = {min(numbers)}")
# ---------------------------------------------
# min(*args):
# *args -> int
# return type -> int

print(f"Max of [12, -1, 0, 25] = {min(12, -1, 0, 25)}")
