# string.isnumeric():
# string -> 'str' data type
# return type -> bool
# '0-9 characters' or 'not empty' -> True

string = "1234"
print(string.isnumeric())
# -------------------------------
string = "abc123"
print(string.isnumeric())
# -------------------------------
string = "12.3"
print(string.isnumeric())
# -------------------------------
string = "-23"
print(string.isnumeric())
# -------------------------------
string = ""
print(string.isnumeric())
