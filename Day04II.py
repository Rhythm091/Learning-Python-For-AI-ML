def num_check():
    while True:
        try:
            num = int(input("Enter a number: "))
            break
        except ValueError:
            print("Invalid input! Please enter a valid number.")

    if num % 2 == 0:
        print("The number you entered is even.")
    else:
        print("The number you entered is odd.")


num_check()
