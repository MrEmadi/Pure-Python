# Prime Number Checker:
# You need to write a function called is_prime() that checks whether if the number passed into it is a prime number or not.
# It should return True or False.

def is_prime(number: int) -> bool:
    if number == 2: return True
    elif number == 1: return False
    elif number < 1: return False
    for i in range(2, number):
        if number % i == 0: return False
    return True

print(f"-4: {is_prime(-4)}")

print(f"0: {is_prime(0)}")

print(f"1: {is_prime(1)}")

print(f"2: {is_prime(2)}")

print(f"4: {is_prime(4)}")

print(f"7: {is_prime(7)}")
