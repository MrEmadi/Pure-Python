# Docstring ("""..."""):
def say_hello():
    """
    Prints a message to say Hello.
    :return: None
    """
    print("Hello, there!")

say_hello()
# ----------------------------------
# Nested Functions:
def outer_function(a, b):
    def inner_function(c, d):
        return c + d
    return inner_function(a, b)

print(outer_function(5, 10))
