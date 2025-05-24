# min(__iterable, key):
# __iterable -> numeric sequence (list, tuple, set, dict) - TypeError
# key = None -> None
# return type -> int

numbers = [12, -9, 0, 44, 1, 13, -7, 25] # :list

print(f"Min of {numbers} = {min(numbers)}")
# ---------------------------------------------
bidders = {
    "Amirhossein": 25,
    "Zahra": 23,
    "Bagher": 65,
    "Narges": 61
}

print(min(bidders, key=bidders.get)) # bidders.get -> values
