def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def generate_primes(start, end):
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes

# Input from the user
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

if start <= end:
    primes = generate_primes(start, end)
    print(f"Prime numbers between {start} and {end}: {primes}")
else:
    print("Invalid range. Start should be less than or equal to End.")
