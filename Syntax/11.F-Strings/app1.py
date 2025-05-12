score = 3456
username = "Amirhossein"

# Without F-String:
print(username + "\'s score is " + str(score))

# With F-String
# Active it -> f"" or f''
# Placeholders -> {...}
print(f"{username}\'s score is {score}")
