num = int(input("Enter an integer: "))
sum_digits = 0

while num > 0:
    sum_digits += num % 10
    num //= 10

print(f"The sum of digits is {sum_digits}.")
