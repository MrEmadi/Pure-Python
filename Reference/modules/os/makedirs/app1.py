# os.makedirs(path, mode, exist_ok):
# os -> class name
# path -> str
# mode = 0o777 -> int
# exist_ok = False -> bool
# return type -> None
# Exists -> FileExistsError

from os import makedirs

makedirs("your/directory")
print(f"done.")
