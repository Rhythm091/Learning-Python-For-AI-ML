def meters_to_feet(meters):
    return meters * 3.28084

def feet_to_meters(feet):
    return feet / 3.28084

def kg_to_lbs(kg):
    return kg * 2.20462

def lbs_to_kg(lbs):
    return lbs / 2.20462

def main():
    print("--- Simple Python Unit Converter ---")
    print("1. Meters to Feet")
    print("2. Feet to Meters")
    print("3. Kilograms to Pounds")
    print("4. Pounds to Kilograms")

    choice = input("\nEnter choice (1-4): ")
    
    if choice not in ['1', '2', '3', '4']:
        print("Invalid choice. Exiting.")
        return

    try:
        value = float(input("Enter the value to convert: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    if choice == '1':
        print(f"{value} meters = {meters_to_feet(value):.2f} feet")
    elif choice == '2':
        print(f"{value} feet = {feet_to_meters(value):.2f} meters")
    elif choice == '3':
        print(f"{value} kg = {kg_to_lbs(value):.2f} lbs")
    elif choice == '4':
        print(f"{value} lbs = {lbs_to_kg(value):.2f} kg")
