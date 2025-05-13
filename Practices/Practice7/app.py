# Write a Pizza Delivery Program:
# - Small pizza(S) -> $15
# - Medium pizza(M) -> $20
# - Large pizza(L) -> $25
# - Pepperoni for small pizza -> +$2
# - Pepperoni for medium or large pizza -> +$3
# - Extra cheese -> +$1

try:
    print("Welcome to Python Pizza Deliveries!\n")
    user_size = input("What size pizza do you want? S, M or L: ")
    user_pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
    user_extra_cheese = input("Do you want extra cheese? Y or N: ")
    if user_size != 'S' and user_size != 'M' and user_size != 'L':
        raise Exception("You must type S, M or L! Try again later.")
    if (user_pepperoni != 'N' and user_pepperoni != 'Y') or (
            user_extra_cheese != 'N' and user_extra_cheese != 'Y'
    ): raise Exception("You must type N or Y! Try again later.")
    total_bill = 15 # S
    if user_size == 'M': total_bill = 20
    elif user_size == 'L': total_bill = 25
    if user_pepperoni == 'Y':
        if user_size == 'S': total_bill += 2
        else: total_bill += 3 # M or L
    if user_extra_cheese == 'Y': total_bill += 1
    print(f"\nTotal bill: ${total_bill}")
except Exception as e: print(f"\nError -> {e}")
