# re.compile(ptr):
# ptr -> str
# return type -> object (Pattern[str])
"""
. -> a character
\d -> numbers (0-9)
\D -> not numbers (0-9)
\w -> letters (a-z and A-Z)
\W -> not letters (a-z and A-Z)
\s -> whitespace
\S -> not whitespace

[] -> a set of characters
[^] -> not a set of characters
[0-9] -> all numbers
[a-z] -> all lowercase letters
^ -> beginning of the string
$ -> end of the string

+ -> 1 or more characters
* -> 0 or more characters
? -> 0 or 1 character
{n, m} -> length of characters
"""

import re

print(re.compile('^\\d+$').match('Amir404'))

print(re.compile('^\\d+$').match('404'))
