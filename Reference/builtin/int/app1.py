# int(obj):
# obj = 0 -> str, int, bool, float (ValueError, TypeError)
# return type -> int
string = '101' # :str (number)
number = int(string)
print(number)

string = '101amir' # :str (text)
number = int(string) # throws ValueError!
print(number)
# ---------------------------------
