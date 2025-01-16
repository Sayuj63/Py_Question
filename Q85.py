import csv

file_name = "example.csv"

try:
    with open(file_name, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
except FileNotFoundError:
    print(f"The file '{file_name}' does not exist.")
