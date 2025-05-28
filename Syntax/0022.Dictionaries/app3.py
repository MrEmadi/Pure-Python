# An alternative way for the match-case statements:

def handle_200():
    return "Ok"

def handle_404():
    return "Not Found"

user_code = int(input('Enter your code: '))
actions = {200: handle_200, 404: handle_404}

print(actions.get(user_code, lambda: "Unknown Error!")())
