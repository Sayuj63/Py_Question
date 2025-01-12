from math import gcd
n = int(input("Enter a range: "))
lcm = 1
for i in range(1, n + 1):
    lcm = lcm * i // gcd(lcm, i)
print(lcm)
