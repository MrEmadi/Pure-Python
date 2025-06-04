# open(file, mode, encoding):
# file -> str
# mode -> str (w, r, a, r+, rb, ...)
# encoding = None -> 'str' or 'None'
# return type -> 'TextIOWrapper' object

try:
    with open('test.txt', 'r', encoding='utf-8') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print('Error -> The file is not found!')
