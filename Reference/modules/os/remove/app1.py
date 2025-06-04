# os.remove(_path):
# os -> class name
# _path -> str
# return type -> None
# Not Found -> FileNotFoundError

from os import remove

remove('test/text.txt') # Delete the file
print('done.')
