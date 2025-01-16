file_name = "example.txt"

try:
    with open(file_name, "r") as file:
        contents = file.read()
    print(contents)
except FileNotFoundError:
    print(f"The file '{file_name}' does not exist.")
