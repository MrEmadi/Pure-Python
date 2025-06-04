# Delete a file:

import os

if os.path.exists('test.txt'):
        os.remove('test.txt')
        print("done.")
else:
    print('Error -> The file is not found!')
