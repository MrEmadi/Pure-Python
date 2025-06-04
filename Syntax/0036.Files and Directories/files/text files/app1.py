# Syntax: 'with ... as ...' -> close the file automatically

# Read a text file (all lines):

try:
    with open('test.txt', 'r', encoding='utf-8') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print('Error -> The file is not found!')
