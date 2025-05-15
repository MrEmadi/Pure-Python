numbers = [12, -9, 0, 44, 1, 13, -7, 25] # :list

print(f"Builtin -> Sum of {numbers} = {sum(numbers)}")
# ----------------------------------------------
start_num = 0
for number in numbers: start_num += number
print(f"Manual -> Sum of {numbers} = {start_num}")
