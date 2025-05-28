# Syntax -> lambda x, y, ...: ...
# A special, simple and short function without name
# -> It has only 1 expression

operations = {
    '+': lambda num1, num2: num1 + num2,
    '-': lambda num1, num2: num1 - num2,
    '*': lambda num1, num2: num1 * num2,
    '/': lambda num1, num2: num1 / num2,
    '**': lambda num1, num2: num1 ** num2
}

user_operation = input("Enter your operation: ")
print(operations.get(user_operation,
                    lambda num1, num2: "Invalid Operation!")(12, 6))
