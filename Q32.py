def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))
print(f"The LCM of {x} and {y} is {lcm(x, y)}.")
