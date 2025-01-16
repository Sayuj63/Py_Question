file_name = "example.txt"

try:
    with open(file_name, "r") as file:
        words = file.read().split()
    longest_word = max(words, key=len)
    print(f"Longest word in '{file_name}': {longest_word}")
except FileNotFoundError:
    print(f"The file '{file_name}' does not exist.")
