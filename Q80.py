file_name = "example.txt"

try:
    with open(file_name, "r") as file:
        line_count = sum(1 for _ in file)
    print(f"Number of lines in '{file_name}': {line_count}")
except FileNotFoundError:
    print(f"The file '{file_name}' does not exist.")
