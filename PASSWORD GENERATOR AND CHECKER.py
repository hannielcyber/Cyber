import string
import random

def generate_password(length):
    """Generate a random password of specified length."""
    all_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

def check_password_strength(password):
    """Check the strength of the given password."""
    password_strength = "Unknown"
    
    if len(password) < 8:
        password_strength = "Very weak. Password should be at least 8 characters long."
    elif password.isalpha():
        password_strength = "Weak. Password should contain a blend of numbers, characters, and special characters."
    elif password.isnumeric():
        password_strength = "Weak. Password should contain a blend of numbers, characters, and special characters."
    elif password.isalnum():
        password_strength = "Medium. Password should contain special characters."
    else:
        password_strength = "Strong. Password contains a blend of numbers, characters, and special characters."
    
    return password_strength

def main():
    print("Password Generator and Strength Checker")
    print("---------------------------------------")
    
    try:
        password_length = int(input("Enter the desired password length: "))
        if password_length <= 0:
            raise ValueError("Password length must be a positive integer.")
    except ValueError as ve:
        print(f"Invalid input: {ve}")
        return

    password = generate_password(password_length)
    print(f"\nGenerated password: {password}")
    print(f"Strength: {check_password_strength(password)}")

if __name__ == "__main__":
    main()
