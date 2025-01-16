file_name = "example.txt"
substring = input("Enter a substring to search for: ")

try:
    with open(file_name, "r") as file:
        lines = file.readlines()
    for i, line in enumerate(lines, start=1):
        if substring in line:
            print(f"Found in line {i}: {line.strip()}")
except FileNotFoundError:
    print(f"The file '{file_name}' does not exist.")
