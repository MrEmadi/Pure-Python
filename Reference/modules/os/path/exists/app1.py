# path.exists(_path):
# path -> class name (os.path)
# _path -> str
# return type -> bool

from os import path

if path.exists('test.txt'):
    print("The file exists.")
else:
    print('Error -> The file is not found!')
