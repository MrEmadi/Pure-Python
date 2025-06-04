# Update a text file (read all lines, then overwrite the file):

try:
    with open('test.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines() # All lines -> list[str]
    # Change the line 3:
    lines[2] = "Tehran\n"
    with open('test.txt', 'w', encoding='utf-8') as file:
        file.writelines(lines)
    print('done.')
except FileNotFoundError:
    print('Error -> The file is not found!')
