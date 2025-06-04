# Check and add a new directory:

from os import path, makedirs

dir_path = "your/directory"
if not path.exists(dir_path):
    makedirs(dir_path)
    print(f"done.")
else:
    print(f"The directory '{dir_path}' already exists!")
