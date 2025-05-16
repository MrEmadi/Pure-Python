# The Gauss Challenge:
# n * (n + 1) / 2 = sum of [1, n]
# 100 * 101 / 2 = 5050 -> [1, 100]
# Work out the total of the numbers between 1 and 100, inclusive of both 1 and 100.

total_numbers = 0
for number in range(1, 101): total_numbers += number
print(f"Total of the numbers between 1 and 100: {total_numbers}")
