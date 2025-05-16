# random.shuffle(mSeq):
# random -> class name
# mSeq -> mutable sequence (list, tuple, set, dict) - TypeError
# return type -> None

import random

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # :list
random.shuffle(numbers)
print(numbers)
# --------------------------------------
