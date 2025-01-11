def fibonacci(n):
    series = [0, 1]
    for i in range(2, n):
        series.append(series[-1] + series[-2])
    return series[:n]

n = int(input("Enter the number of Fibonacci numbers: "))
print(fibonacci(n))