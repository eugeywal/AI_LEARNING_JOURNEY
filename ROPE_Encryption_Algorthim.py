print("\033[H\033[2J", end="")
import random
import sys

# Set encoding for console output to avoid display issues with non-ASCII characters
# sys.stdout.reconfigure(encoding='utf-8') 

# --- 1. Key Generation Functions ---

def generate_odd_key():
    """Generates a random odd key between 1 and (2 ** 8)."""
    return 2 * random.randint(1, (2 ** 8)) + 1

def generate_even_key():
    """Generates a random even key between 1 and (2 ** 8)."""
    return 2 * random.randint(1, (2 ** 8))

def generate_prime_key():
    """Generates a random prime key between 2 and (2 ** 8)."""
    while True:
        p = random.randint(2, (2 ** 8)) 
        # Primality check
        is_prime = True
        for i in range(2, int(p**0.5) + 1):
            if p % i == 0:
                is_prime = False
                break
        if is_prime:
            return p

# --- 2. Cipher Functions ---

def get_base(char):
    """Determines the base ASCII value ('A' or 'a') for a character."""
    if char.isupper():
        return ord('A')
    elif char.islower():
        return ord('a')
    return None

def encrypt_char(char, key):
    """Encrypts a single character and returns the encrypted character, base, and key."""
    
    base = get_base(char)
    
    if base is None:
        # Return character as is for non-alphabetic chars
        return char, ord(char), -128 
    
    # Cipher Equation: C = ((O - B) * K) + B
    cipher_ord = ((ord(char) - base) * key) + base
    
    # Return encrypted character, base, and key
    return chr(cipher_ord), base, key

def apply_alternating_cipher(plain_text):
    """Applies the alternating cipher, returning the ciphertext, used keys, and the base."""
    
    cipher_text = ""
    used_keys = []
    # Base used for the first alphabetic character determines the base for all others
    initial_base = 0 
    key_generators = [generate_odd_key, generate_prime_key, generate_even_key]
    
    for i, char in enumerate(plain_text):
        if char == " ":
            cipher_text += "?"
            used_keys.append(-128) # Special key for space
            continue
        else:
            # 1. Generate the alternating key
            cipher_key = key_generators[i % 3]()
            
            # 2. Encrypt
            encrypted_char, base_used, key = encrypt_char(char, cipher_key)
            
            # 3. Store result and key
            cipher_text += encrypted_char
            used_keys.append(key)
            
            # 4. Store the base for decryption if this is the first alphabetic character
            if initial_base == 0 and base_used not in [0, -128]:
                initial_base = base_used
                
    return cipher_text, used_keys, initial_base

# --- 3. Main Execution Function ---

def main_encryption_run(plain_text):
    """Runs the full encryption process for the entire message."""
    
    if not plain_text:
        print("Input text cannot be empty.")
        return

    # 1. Encrypt the text
    final_cipher_text, used_keys, base = apply_alternating_cipher(plain_text)
    
    # 2. Print Encryption Results (to be saved for decryption)
    print("\n" + "=" * 60)
    print("--- ENCRYPTION RESULTS ---")
    print(f"Original Text: {plain_text}")
    print(f"Ciphertext:    {final_cipher_text}")
    print(f"Used Keys:     {used_keys}")
    print(f"Base Used:     {base} (e.g., ord('A')=65 or ord('a')=97)")
    print("=" * 60 + "\n")
    print("!!! SAVE THE Ciphertext, Used Keys, and Base Used for Decryption !!!")

# --- 4. Starting Point (User Input) ---

# Clear screen (optional)
# print("\033[H\033[2J", end="")

user_input = input("Please enter the message to encrypt: ")

# Run the encryption on the user's message
main_encryption_run(user_input)