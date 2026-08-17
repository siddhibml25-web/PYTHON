# Simple Password Generator - Simple Version
import random
import string

def password_generator():
    print("--- SIMPLE PASSWORD GENERATOR ---")
    
    length = int(input("Enter password length (e.g., 8, 12): "))
    
    use_upper = input("Include Uppercase letters (y/n)? ").lower() == 'y'
    use_digits = input("Include Digits (y/n)? ").lower() == 'y'
    use_special = input("Include Special characters (y/n)? ").lower() == 'y'

    # Characters pool banana (by default lowercase always included)
    chars = string.ascii_lowercase

    if use_upper:
        chars += string.ascii_uppercase
    if use_digits:
        chars += string.digits
    if use_special:
        chars += "!@#$%^&*()-_"

    # Password generate karna
    password = ""
    for _ in range(length):
        password += random.choice(chars)

    print("\n--- RESULT ---")
    print("Generated Password:", password)

if __name__ == "__main__":
    password_generator()
