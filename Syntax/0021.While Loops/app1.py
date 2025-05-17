# Syntax

# while <conditionIsTrue>:
#     ...

is_a_number = True
while is_a_number:
    user_number = input("Enter a whole number or \"e\" for exit: ")
    if user_number.isnumeric() or user_number == 'e':
        is_a_number = False
        if user_number.isnumeric():
            print("Yes!")
        if user_number == 'e':
            print("Bye!")
# -------------------------------------------
