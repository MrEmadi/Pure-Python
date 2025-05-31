# try-except Syntax:

try:
    age = int(input('How old are you? '))
    print(f"You are {age} years old!")
except ValueError as e:
    print(e)
# --------------------------------------
# try-except-finally Syntax:

try:
    price = int(input('How much do you have? '))
    print(f"Price is ${price}!")
except ValueError as e:
    print(e)
finally:
    print('Goodbye!')
