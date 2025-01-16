source_file = "source.txt"
destination_file = "destination.txt"

try:
    with open(source_file, "r") as src:
        contents = src.read()
    with open(destination_file, "w") as dest:
        dest.write(contents)
    print(f"Contents copied from '{source_file}' to '{destination_file}'.")
except FileNotFoundError:
    print(f"The file '{source_file}' does not exist.")
