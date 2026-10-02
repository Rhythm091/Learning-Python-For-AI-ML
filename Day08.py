def num_sum():
    while True:
        try:
            num = int(input("Enter the number: "))
            break
        except ValueError:
            print("Invalid input! Please enter a valid number.")

    for i in range(1, num + 1):
        total = num + i
        print(f"The sum of {num} and {i} is {total}.")

num_sum()
