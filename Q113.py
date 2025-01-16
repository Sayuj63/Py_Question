from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filtering even numbers
filtered = list(filter(lambda x: x % 2 == 0, numbers))
print("Filtered Even Numbers:", filtered)

# Summing the filtered numbers
sum_of_evens = reduce(lambda x, y: x + y, filtered)
print("Sum of Even Numbers:", sum_of_evens)
