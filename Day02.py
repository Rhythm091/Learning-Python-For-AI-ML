import random

def pass_gen():
    while True:
        try:
            length = int(input("Enter password length: "))
            
            if length <= 0:
                print("Password length must be greater than zero. Try again.")
                continue
                
            break
            
        except ValueError:
            print("Invalid input! Please enter a number.")

    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=[]{}|;:,.<>?/~`"

    password = ""
    for _ in range(length):
        password += random.choice(characters)
        
    return password

print(f"Generated password: {pass_gen()}")