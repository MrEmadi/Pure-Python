# list.index(value, start, stop):
# list -> 'list' data type
# value -> T (str, int, ...)
# start = 0 -> int
# stop = sys.maxsize -> int
# return type -> int
# not found -> ValueError

letters = ['V', 'X', 'O', 'A', 'W', 'O']

print(letters.index('X'))

print(letters.index('O'))

print(letters.index('O', 3, 6))
