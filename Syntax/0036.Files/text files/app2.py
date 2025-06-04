# Read a text file (line by line):

try:
    with open('test.txt', 'r', encoding='utf-8') as file:
        counter = 1
        for line in file:
            print(f'Line {counter}: {line.strip()}')
            counter += 1
except FileNotFoundError:
    print('Error -> The file is not found!')
