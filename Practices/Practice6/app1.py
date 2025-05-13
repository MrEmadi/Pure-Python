# Numbers: Even or Odd? Check odd or even.

try:
    number = int(input("Enter a whole number: "))
    status = "odd"
    if number % 2 == 0: status = "even"
    print(f"{number} is {status}.")
except Exception as e: print(f"\nError -> {e}")
