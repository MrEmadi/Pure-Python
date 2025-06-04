# Write a text file (Overwrite the file):

try:
    with open('test.txt', 'w', encoding='utf-8') as file:
        file.write("Zahra Emadi\n23\nYazd")
    print('done.')
except FileNotFoundError:
    print('Error -> The file is not found!')
