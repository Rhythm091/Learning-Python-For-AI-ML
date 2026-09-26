import random
import string

def pass_gen():
    while True:
        try:
            length = int(input("\nEnter password length: "))
            if length >= 4:
                break
            print("Password length should be at least 4 characters.")
        except ValueError:
            print("Please enter a valid number.")

    include_numbers = input("Include numbers? (y/n): ").lower().startswith('y')
    include_symbols = input("Include symbols? (y/n): ").lower().startswith('y')

    char_pool = string.ascii_letters
    
    password_chars = [random.choices(string.ascii_letters)]

    if include_numbers:
        char_pool += string.digits
        password_chars.append(random.choice(string.digits))

    if include_symbols:
        char_pool += string.punctuation
        password_chars.append(random.choice(string.punctuation))

    remaining_length = length - len(password_chars)

    for _ in range(remaining_length):
        password_chars.append(random.choice(char_pool))

    random.shuffle(password_chars)
    return "".join(password_chars)

print(f"Generated password: {pass_gen()}")