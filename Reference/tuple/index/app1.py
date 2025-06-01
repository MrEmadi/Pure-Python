# tuple.index(value, start, stop):
# tuple -> 'tuple' data type
# value -> T (str, int, float, ...)
# start = 0 -> int
# stop = sys.maxsize -> int
# return type -> int
# not found -> ValueError

numbers = (12, 8, 9, -7, 12, 0, 13, 12, 0)

print(numbers.index(12))

print(numbers.index(12, 5))
