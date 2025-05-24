# Functions with Output:

def sum_two_numbers(number1: int, number2: int):
    return number1 + number2

print(f"Sum: {sum_two_numbers(10, 15)}")
# ------------------------------------------------
def format_name(first: str, last: str):
    return f"{first} {last}".title()

print(format_name("amirhossein", "emadi"))
