# os.rmdir(_path):
# os -> class name
# _path -> str
# return type -> None
# -> Not Found: FileNotFoundError
# -> Not Empty: OSError

from os import rmdir

rmdir('test') # Remove the empty directory
print('done.')
