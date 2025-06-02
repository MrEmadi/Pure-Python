# Variable naming conventions:
# 1. English letters (uppercase and lowercase)
# 2. Numbers (0-9) -> It must be not at the beginning of the name
# 3. Underline (_)
# 4. variable name: snake case

_var1 = True
Var2 = 5
# 2war = 32 -> wrong!
readable = 'yes'
# user name = 'Amir' -> wrong!
# user-name = "Amir Emadi" # wrong! -> 'kebab case'
# -------------------------------------
# bad naming (It's not readable!):
n = "Amirhossein"
a = 25
c = "Gorgan"

str = "some text!" # bad naming -> reserved keyword in Python!

# good naming (It's readable):
username = "Amirhossein"
age = 25
city = "Gorgan"

user_name = "Amirhossein Emadi" # good naming -> 'snake case'
userName = "Zahra Emadi" # good naming -> 'camel case'
UserName = "Bagher Emadi" # good naming -> 'pascal case'
