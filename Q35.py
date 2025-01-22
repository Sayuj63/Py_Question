def sum_of_series(n):
    total = 0
    for i in range(1, n + 1):
        total += 1 / i  # Add the reciprocal of each number to the total
    return total

# Input from the user
num = int(input("Enter the value of n: "))

# Ensure the input is valid
if num > 0:
    result = sum_of_series(num)
    print(f"The sum of the series 1 + 1/2 + 1/3 + ... + 1/{num} is {result:.4f}")
else:
    print("Please enter a positive integer.")
