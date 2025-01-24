def collatz_sequence(n):
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n //= 2  # Divide by 2 if even
        else:
            n = 3 * n + 1  # Multiply by 3 and add 1 if odd
        sequence.append(n)
    return sequence

# Input from the user
num = int(input("Enter a positive integer: "))

if num > 0:
    sequence = collatz_sequence(num)
    print(f"The Collatz sequence starting with {num}: {sequence}")
else:
    print("Please enter a positive integer.")
