# Python Scopes:

# Global Scope:
age = 12

def test_func():
    # Local Scope - inside the block of codes:
    age = 25
    print(f"Inner: {age}")

test_func()
print(f"Outer: {age}")

# Note: There is no Block Scope in Python!
