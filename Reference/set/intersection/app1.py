# set.intersection(*iter):
# set -> 'set' data type
# *iter = [] -> iterable (list, set, tuple, str)
# return type -> set[T]

names = {'Amir', 'Zahra', 'Bagher', 'Narges'}

print(f'Diff: {names.intersection()}')

print(f'Diff: {names.intersection(['Ali', 'Mehdi', 'Zahra'])}')

print(f'Diff: {names.intersection(('Amin', 'Amir', 'Zahra'))}')

print(f'Diff: {names.intersection(('Amir', 'Zahra'), ['Bagher'])}')
