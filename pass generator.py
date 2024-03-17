import random
import string

def generate_password(length, num_alphabets, num_numbers, num_symbols):
    if length < num_alphabets + num_numbers + num_symbols:
        print("Invalid input: Total length cannot be less than the sum of alphabets, numbers, and symbols.")
        return None

    alphabets = ''.join(random.choices(string.ascii_letters, k=num_alphabets))

    numbers = ''.join(random.choices(string.digits, k=num_numbers))

    symbols = ''.join(random.choices(string.punctuation, k=num_symbols))

    password_characters = alphabets + numbers + symbols
    password_characters = ''.join(random.sample(password_characters, len(password_characters)))

    remaining_length = length - len(password_characters)
    additional_characters = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=remaining_length))

    password = password_characters + additional_characters

    password = ''.join(random.sample(password, len(password)))

    return password

length = int(input("Enter the desired length of the password: "))
num_alphabets = int(input("Enter the number of alphabets in the password: "))
num_numbers = int(input("Enter the number of numbers in the password: "))
num_symbols = int(input("Enter the number of special symbols in the password: "))

password = generate_password(length, num_alphabets, num_numbers, num_symbols)

if password:
    print("Generated Password:", password)
