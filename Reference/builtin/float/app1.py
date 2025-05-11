# float(obj):
# obj = 0.0 -> str, int, bool, float (ValueError, TypeError)
# return type -> float
weight_in_pounds = input("Type your weight (lbs): ")
weight_in_kilograms = float(weight_in_pounds) * 0.45
print("Your weight (kg): " + str(weight_in_kilograms))
