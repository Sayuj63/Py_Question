from multiprocessing import Pool

def square(x):
    return x ** 2

numbers = [1, 2, 3, 4, 5]

with Pool() as pool:
    results = pool.map(square, numbers)

print("Squared Results:", results)
