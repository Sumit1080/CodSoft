import random
import string

def generate_password(length):
    # All possible characters (uppercase, lowercase, digits, symbols)
    characters = string.ascii_letters + string.digits + string.punctuation

    # Randomly choose characters and join them to form the password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Step 1: Ask user for password length
try:
    length = int(input("Enter the desired password length: "))
    
    if length <= 0:
        print("Please enter a positive number.")
    else:
        # Step 2: Generate password
        password = generate_password(length)

        # Step 3: Display the password
        print("Generated Password:", password)

except ValueError:
    print("Please enter a valid number.")
