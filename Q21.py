def count_vowels(string):
    vowels = "aeiouAEIOU"
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count

text = input("Enter a string: ")
print(f"The number of vowels in the string is {count_vowels(text)}.")
