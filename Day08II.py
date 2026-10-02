def sum_fact():
    while True:
        try:
            num = int(input("Enter a number: "))
            break
        except ValueError:
            print("Invalid input! Please enter a valid number.")

    total = 0
    for i in range(1, num + 1):
        total += i
        print(f"The sum of numbers from 1 to {i} is {total}.")

sum_fact()