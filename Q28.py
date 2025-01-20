print("Numbers from 1 to 10 with conditions:")
for i in range(1, 11):
    if i % 3 == 0:
        continue
    if i == 9:
        break
    print(i)
