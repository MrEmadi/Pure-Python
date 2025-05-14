# list.extend(__iterable):
# list -> 'list' data type
# __iterable -> Iterable (list, tuple, dict, set, str)
# return type -> None

names = ['Ali', 'Reza', 'Amir', 'Zahra', 'Zeynab']

names.extend(["Bagher", "Mehdi"]) # :list
names.extend("USA") # :str

print(names)
