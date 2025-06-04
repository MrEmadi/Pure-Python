# Write a text file (Append the file):

try:
    with open('test.txt', 'a', encoding='utf-8') as file:
        file.write("\nShe is a nurse.")
    print('done.')
except FileNotFoundError:
    print('Error -> The file is not found!')
