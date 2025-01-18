def round_float(num):
    return int(num * 100 + 0.5) / 100

float_num = float(input("Enter a float number: "))
print(f"Rounded to 2 decimal places: {round_float(float_num)}")
