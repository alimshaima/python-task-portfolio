Temperature Conversion (Celsius ↔ Fahrenheit)
temp = float(input("Enter the temperature: "))
unit = input("Enter the unit (C for Celsius, F for Fahrenheit): ")

if unit == "C":
    convert = (temp * 9/5) + 32
    print(f"{temp}°C = {convert}°F")
elif unit == "F":
    convert = (temp - 32) * 5/9
    print(f"{temp}°F = {convert}°C")
else:
    print("Invalid unit!")
