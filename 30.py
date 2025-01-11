def count_occurrences(lst, x): return lst.count(x)
lst = list(map(int, input("Enter the list elements separated by space: ").split()))
x = int(input("Enter the element to count: "))
print(count_occurrences(lst, x))