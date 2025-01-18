def string_length(s):
    count = 0
    for char in s:
        count += 1
    return count

user_string = input("Enter a string: ")
print(f"Length of the string: {string_length(user_string)}")
