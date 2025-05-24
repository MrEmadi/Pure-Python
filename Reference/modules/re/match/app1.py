# ptr.match(string, start, end):
# ptr -> 'Pattern[str]' object
# string -> str
# start = 0 -> int
# end = sys.maxsize -> int
# return type -> object (Match[str]) or None
# not found -> None

import re

print(re.compile('^\\d+$').match('Amir404'))

print(re.compile('^\\d+$').match('404'))
