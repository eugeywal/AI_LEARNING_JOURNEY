import random
import sys

print("\033[H\033[2J", end="")

# Set encoding for console output to avoid display issues with non-ASCII characters
# Note: This line might not be necessary depending on the user's environment, 
# but is often helpful when mixing inputs/outputs.
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

# --- 2. Cipher and Decipher Functions ---

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

def decrypt_char(cipher_char, base, key):
    """Decrypts a single character using the base and key."""
    
    cipher_value = ord(cipher_char)
    
    # Decipher Equation: O = ((C - B) / K) + B
    # The result is cast to int as ASCII values are integers
    original_ord_value = int(((cipher_value - base) / key) + base)
    
    # Convert the restored ASCII value back to a character
    return chr(original_ord_value)

def apply_alternating_cipher(plain_text):
    """Applies the alternating cipher, returning the ciphertext, used keys, and the base."""
    global cipher_text
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

def main_algorithm_run(plain_text):
    """Runs the full encryption and decryption process for the entire message."""
    
    if not plain_text:
        print("Input text cannot be empty.")
        return

    # 1. Encrypt the text
    final_cipher_text, used_keys, base = apply_alternating_cipher(plain_text)
    
    # 2. Print Encryption Results
    print("\n" + "=" * 60)
    print(f"Original Text: {plain_text}")
    print(f"Ciphertext:    {final_cipher_text}")
    print(f"Used Keys:     {used_keys}")
    print(f"Base Used:     {base} (e.g., ord('A')=65 or ord('a')=97)")
    print("=" * 60 + "\n")

    # 3. Decryption Process
    decrypted_text = ""
    cipher_text_index = 0
    
    print("--- Decryption Process ---")
    
    for i, key in enumerate(used_keys):
        
        # Handle space character first
        if key == -128:
            decrypted_text += " "
            cipher_text_index += 1
            continue
        
        # Get the current ciphertext character
        cipher_char = final_cipher_text[cipher_text_index]
        key_for_decryption = key
        
        # Use the stored base. Since the base is determined by case ('A' or 'a'), 
        # we need to determine the correct base for the current character being decrypted.
        
        # Get the actual base used for this specific cipher char
        current_base = get_base(plain_text[cipher_text_index]) 
        
        # Fallback to the initial base if get_base returns None (shouldn't happen for the key != -128 case)
        if current_base is None:
             current_base = base # Use the stored initial base
        
        # Decrypt
        try:
            decrypted_char = decrypt_char(cipher_char, current_base, key_for_decryption)
            decrypted_text += decrypted_char
        except Exception as e:
            decrypted_text += "[ERR]"
            print(f"Error decrypting char '{cipher_char}' with key {key}: {e}")
            
        cipher_text_index += 1
        
    print(f"\nRestored Text: {decrypted_text}")
    print("-" * 60)
    
    # 4. Verification
    if decrypted_text == plain_text:
        print("✅ Decryption successful. Restored text matches original.")
    else:
        print("❌ Decryption failed. Restored text does NOT match original.")

# --- 4. Starting Point (User Input) ---

# Get message input from the user
user_input = input("Please enter the message to encrypt and decrypt: ")

# Run the algorithm once on the user's message
main_algorithm_run(user_input)

print(cipher_text)