file_name = "example.txt"
text = input("Enter a line of text to append: ")

with open(file_name, "a") as file:
    file.write(text + "\n")

print(f"Text appended to '{file_name}'.")
