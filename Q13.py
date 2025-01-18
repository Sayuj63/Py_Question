temp = float(input("Enter temperature: "))
choice = input("Convert to (C)elsius or (F)ahrenheit? ").upper()

if choice == 'C':
    converted = (temp - 32) * 5/9
    print(f"Temperature in Celsius: {converted:.2f}°C")
elif choice == 'F':
    converted = (temp * 9/5) + 32
    print(f"Temperature in Fahrenheit: {converted:.2f}°F")
else:
    print("Invalid choice.")
