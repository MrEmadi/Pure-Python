# path.split(_path):
# path -> class name (os.path)
# _path -> str
# return type -> tuple

from os import path

print(path.split('example/api/test.cpp'))

print(path.split('/test.cpp'))

print(path.split('test.cpp'))
