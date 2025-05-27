# Modify a local scope

# Way 1 - global keyword:
name = "Amir404"

def change_name_1():
    global name
    name = "Amir403"

change_name_1()
print(name)
# ---------------------------------------
# Way 2 - return function with a parameter (recommended):
name = "Amir"

def change_name_2(old_name: str) -> str:
    return old_name + "403"

print(change_name_2(name))
