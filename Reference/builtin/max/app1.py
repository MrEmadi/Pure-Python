# max(__iterable, key):
# __iterable -> numeric sequence (list, tuple, set, dict) - TypeError
# key = None -> None
# return type -> int

numbers = [12, -9, 0, 44, 1, 13, -7, 25] # :list

print(f"Max of {numbers} = {max(numbers)}")
# ---------------------------------------------
bidders = {
    "Amirhossein": 25,
    "Zahra": 23,
    "Bagher": 65,
    "Narges": 61
}

print(max(bidders, key=bidders.get)) # bidders.get -> values
