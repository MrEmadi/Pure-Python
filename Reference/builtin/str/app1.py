# str(obj):
# obj = "" -> str, int, bool, float (ValueError, TypeError)
# return type -> str
weight_in_pounds = input("Type your weight (lbs): ")
weight_in_kilograms = float(weight_in_pounds) * 0.45
print("Your weight (kg): " + str(weight_in_kilograms))
