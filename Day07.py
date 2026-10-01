def multi_table():
    while True:
        try:
            num = int(input("Enter a number: "))
            print(f"Multiplication table for {num}:")

            for i in range(1, 11):
                result = num * i
                print(f"{num} x {i} = {result}")

            break

        except ValueError:
            print("Invalid input. Please enter a valid number.")


multi_table()