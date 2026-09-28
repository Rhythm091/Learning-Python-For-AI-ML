def num_checker():
    while True:
        try:
            num = int(input("Enter a number: "))
            break
        except ValueError:
            print("Invalid input! Please enter a valid number.")

    if num == 0:
        print("The Number you entered is zero.")
    elif num > 0:
        print("The Number you entered is positive.")
    else:
        print("The Number you entered is negative.")


num_checker()