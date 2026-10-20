print("Welcome to the Temperature Converter!")

fahrenheit = float(input("Enter Fahrenheit: "))

celsius = (fahrenheit - 32) * 5 / 9

print(f"{fahrenheit}°F = {celsius:.2f}°C")

print("Thank you for using our converter!")