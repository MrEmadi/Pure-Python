# list.sort(__list, key, reverse):
# list -> 'list' data type
# __list -> list
# key = None -> None (lambda function)
# reverse = False -> bool
# return type -> None

# List of Numbers: lower (0) -> greater (9)
# List of Strings: A -> Z

numbers = [12, 0, -9, 10, 100, 101, 94, -65, 102]
list.sort(numbers)
print(numbers)
# -----------------------------------------
names = ['Zahra', 'Ali', 'Amin', 'Amir', 'Mina', 'Sara', 'Reza', 'Rad']
list.sort(names)
print(names)
# -----------------------------------------
users = [
    {
        'name': 'Zahra',
        'age': 23
    },
    {
        'name': 'Bagher',
        'age': 65
    },
    {
        'name': 'Narges',
        'age': 62
    },
    {
        'name': 'Amir',
        'age': 25
    }
]
list.sort(users, key=lambda user: user['age'])
print(users)
