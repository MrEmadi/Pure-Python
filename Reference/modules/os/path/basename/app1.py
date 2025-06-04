# path.basename(_path):
# path -> class name (os.path)
# _path -> str
# return type -> str

from os import path

print(path.basename('example/api/test.cpp'))

print(path.basename('/test.cpp'))

print(path.basename('test.cpp'))
