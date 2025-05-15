# range(a, b, step)
# a = 0 -> int
# b -> int
# step = 1 -> int
# return type -> 'range' data type
# [a, b)

numbers = range(12)
for num in numbers: print(f"[{num}]")

print(type(numbers))
# ----------------------------------------
for number in range(0, 25): print(f"[0, 25) => {number}")
# ----------------------------------------
for number in range(0, 12, 4): print(f"[0, 12) => {number}")
# ----------------------------------------
for number in range(12, 0, -1): print(f"[12, 0) => {number}")
