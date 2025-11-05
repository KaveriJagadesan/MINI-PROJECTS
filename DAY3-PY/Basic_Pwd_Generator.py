import random
import string

def generate_password(length, use_numbers=True, use_symbols=True):
    """
    Generates a random password of a specified length and complexity.

    Args:
        length (int): The desired length of the password.
        use_numbers (bool): Include numbers in the password if True.
        use_symbols (bool): Include symbols in the password if True.

    Returns:
        str: A randomly generated password.
    """
    # 1. Define character sets
    lowercase_chars = string.ascii_lowercase
    uppercase_chars = string.ascii_uppercase
    numbers = string.digits
    symbols = string.punctuation

    # 2. Build the character pool based on complexity arguments
    char_pool = lowercase_chars + uppercase_chars
    if use_numbers:
        char_pool += numbers
    if use_symbols:
        char_pool += symbols

    # Handle the case where no character types are selected
    if not char_pool:
        raise ValueError("At least one character type (letters, numbers, or symbols) must be enabled.")

    # 3. Create the password using a loop
    password = ""
    for _ in range(length):
        password += random.choice(char_pool)

    return password

# --- Testing the function ---
if __name__ == "__main__":
    # Test 1: Generate a password with all character types
    print("--- Test 1: Complex Password (12 characters) ---")
    password_complex = generate_password(length=12, use_numbers=True, use_symbols=True)
    print(f"Generated Password: {password_complex}")
    print("-" * 40)

    # Test 2: Generate a password without numbers
    print("--- Test 2: Letters and Symbols Only (8 characters) ---")
    password_no_numbers = generate_password(length=8, use_numbers=False, use_symbols=True)
    print(f"Generated Password: {password_no_numbers}")
    print("-" * 40)

    # Test 3: Generate a password with only letters and numbers
    print("--- Test 3: Letters and Numbers Only (10 characters) ---")
    password_no_symbols = generate_password(length=10, use_numbers=True, use_symbols=False)
    print(f"Generated Password: {password_no_symbols}")
    print("-" * 40)

    # Test 4: Generate a password with letters only
    print("--- Test 4: Letters Only (15 characters) ---")
    password_letters_only = generate_password(length=15, use_numbers=False, use_symbols=False)
    print(f"Generated Password: {password_letters_only}")
    print("-" * 40)
