while True:
    try:
        number = int(input("Enter a number: "))
        print(f"Valid number entered: {number}")
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.")
