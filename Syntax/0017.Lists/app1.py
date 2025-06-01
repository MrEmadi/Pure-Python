# Lists:
# - Syntax -> list_name = [value1, value2, value3, ...]
# - Indexed
# - Ordered
# - Changeable
# - Repeat is allowed
# - IndexError

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
names = ['Ali', 'Reza', 'Amir', 'Zahra', 'Zeynab']
points = [12.7, -98.5, 0.0, 5.43, -4.12]
# ----------------------------------------------
# Start Index -> 0 (left to right):
print(numbers[5])
print(names[3])
print(points[1])

# Start Index -> -1 (right to left):
print(numbers[-5])
print(names[-3])
print(points[-1])
# ----------------------------------------------
# Edit a value:
names[2] = "Bagher"
print(names)
