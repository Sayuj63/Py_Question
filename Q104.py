import os

current_directory = os.getcwd()
files_and_directories = os.listdir(current_directory)

print("Files and Directories in Current Directory:")
for item in files_and_directories:
    print(item)
