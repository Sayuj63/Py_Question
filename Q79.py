file_name = "example.txt"

try:
    with open(file_name, "r") as file:
        contents = file.read()
    word_count = len(contents.split())
    print(f"Number of words in '{file_name}': {word_count}")
except FileNotFoundError:
    print(f"The file '{file_name}' does not exist.")
