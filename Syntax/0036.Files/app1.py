# Delete a file:

from os import path, remove

if path.exists('test.txt'):
    remove('test.txt')
    print("done.")
else:
    print('Error -> The file is not found!')
