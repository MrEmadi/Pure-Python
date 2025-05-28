# Default Statements -> or keyword:

user_code = input("Enter your code: ")
result = user_code or "Unknown!" # if "" -> return Unknown!
print(result)
# --------------------------------
user_code = int(input("Enter your code: "))
result = user_code or 999 # if 0 -> return 999
print(result)
