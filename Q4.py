a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

a, b = b, a  # Swapping without a temporary variable
print(f"Swapped values: a = {a}, b = {b}")
