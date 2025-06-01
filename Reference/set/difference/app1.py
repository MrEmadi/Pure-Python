# set.difference(*iter):
# set -> 'set' data type
# *iter = [] -> iterable (list, set, tuple, str)
# return type -> set[T]

names = {'Amir', 'Zahra', 'Bagher', 'Narges'}

print(f'Diff: {names.difference()}')

print(f'Diff: {names.difference(['Ali', 'Mehdi', 'Zahra'])}')

print(f'Diff: {names.difference(('Amin', 'Amir', 'Zahra'))}')

print(f'Diff: {names.difference(('Amir', 'Zahra'), ['Bagher'])}')
