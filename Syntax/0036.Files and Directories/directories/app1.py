# Remove an empty directory:

# -> Not Found: FileNotFoundError
# -> Not Empty: OSError

from os import rmdir

rmdir('test')
print('done.')
