# if-elif-else:
age = int(input("How old are you? "))
height = int(input("What is your height in cm? "))

if age > 18:
    print("All is fine!")
elif age == 18:
    print("Come back soon!")
else:
    print("You don't have permission to do that!")
# ----------------------------------------------
# Nested if-else:
if age > 18:
    if height >= 110:
        print("You can ride the rollercoaster!")
    else:
        print("You can't ride the rollercoaster!")
