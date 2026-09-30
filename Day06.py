def fahrenheit_converter():
    while True:
        try:
            celsius = float(input("Enter temperature in Celsius: "))
            break
        except ValueError:
            print("Invalid input! Please enter a valid number.")

    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C is equal to {fahrenheit}°F.")


def celsius_converter():
    while True:
        try:
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            break
        except ValueError:
            print("Invalid input! Please enter a valid number.")

    celsius = (fahrenheit - 32) * 5/9
    print(f"{fahrenheit}°F is equal to {celsius}°C.")


def celsius_kelvin():
    while True:
        try:
            celsius = float(input("Enter temperature in Celsius: "))
            break
        except ValueError:
            print("Invalid input! Please enter a valid number.")

    kelvin = celsius + 273.15
    print(f"{celsius}°C is equal to {kelvin} K.")


def kelvin_celsius():
    while True:
        try:
            kelvin = float(input("Enter temperature in Kelvin: "))

            if kelvin < 0:
                print("Kelvin cannot be below 0. Please enter a valid temperature.")
                continue

            break

        except ValueError:
            print("Invalid input! Please enter a valid number.")

    celsius = kelvin - 273.15
    print(f"{kelvin} K is equal to {celsius}°C.")


print("\n===== Temperature Converter =====")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
print("3. Celsius to Kelvin")
print("4. Kelvin to Celsius")

choice = input("\nEnter your choice (1-4): ")

if choice == "1":
    fahrenheit_converter()

elif choice == "2":
    celsius_converter()

elif choice == "3":
    celsius_kelvin()

elif choice == "4":
    kelvin_celsius()

else:
    print("Invalid input! Please enter a valid option (1, 2, 3, or 4).")