def is_armstrong(num):
    # Check if the number is a 3-digit number
    if num < 100 or num > 999:
        return False

    # Split the number into digits
    digits = [int(digit) for digit in str(num)]
    
    # Calculate the sum of cubes of the digits
    armstrong_sum = sum(digit ** 3 for digit in digits)
    
    # Check if the sum equals the original number
    return armstrong_sum == num

# Input from the user
number = int(input("Enter a 3-digit number: "))

# Output the result
if is_armstrong(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")
