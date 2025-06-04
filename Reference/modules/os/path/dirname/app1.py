# path.dirname(_path):
# path -> class name (os.path)
# _path -> str
# return type -> str

from os import path

print(path.dirname('example/api/test.cpp'))

print(path.dirname('/test.cpp'))

print(path.dirname('test.cpp'))
