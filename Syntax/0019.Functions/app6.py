# *args in functions -> with '*' symbol:

def sum_numbers(init_number: int, *numbers) -> int:
    result = init_number
    for number in numbers:
        result += number
    return result

print(sum_numbers(20, 2, 3, -7))
