print("\033[H\033[2J", end="")
import sys

# Set encoding for console output to avoid display issues with non-ASCII characters
# sys.stdout.reconfigure(encoding='utf-8') 

# --- 1. Base Function (Copied from Encryption) ---

def get_base(char):
    """Determines the base ASCII value ('A' or 'a') for a character."""
    if char.isupper():
        return ord('A')
    elif char.islower():
        return ord('a')
    return None

# --- 2. Decipher Functions ---

def decrypt_char(cipher_char, base, key):
    """Decrypts a single character using the base and key."""
    
    cipher_value = ord(cipher_char)
    
    # Decipher Equation: O = ((C - B) / K) + B
    # The result is cast to int as ASCII values are integers
    original_ord_value = int(((cipher_value - base) / key) + base)
    
    # Convert the restored ASCII value back to a character
    return chr(original_ord_value)

def main_decryption_run(cipher_text, used_keys, base, original_plain_text):
    """Runs the full decryption process."""
    
    if not cipher_text or not used_keys or base == 0:
        print("Ciphertext, keys, and base are required for decryption.")
        return

    # 1. Decryption Process
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
        cipher_char = cipher_text[cipher_text_index]
        key_for_decryption = key
        
        # Determine the correct base for the current character being decrypted.
        
        # Get the actual base used for this specific cipher char
        # NOTE: This requires the original_plain_text to correctly determine case. 
        # In a real-world scenario, the base/case information is usually derived 
        # from the ciphertext itself or the key, but in this specific code structure,
        # we rely on the case of the *original* character.
        
        # Fallback logic to determine base for decryption (using a simplified method)
        if cipher_char.isupper():
             current_base = ord('A')
        elif cipher_char.islower():
             current_base = ord('a')
        else:
             current_base = base # Use the stored initial base if case cannot be determined (e.g., if char is '?' instead of a letter)

        # Decrypt
        try:
            decrypted_char = decrypt_char(cipher_char, current_base, key_for_decryption)
            decrypted_text += decrypted_char
        except Exception as e:
            decrypted_text += "[ERR]"
            print(f"Error decrypting char '{cipher_char}' with key {key}: {e}")
            
        cipher_text_index += 1
        
    print("\n" + "=" * 60)
    print(f"Restored Text: {decrypted_text}")
    print("=" * 60)

    # 3. Verification
    if decrypted_text == original_plain_text:
        print("✅ Decryption successful. Restored text matches original.")
    else:
        print("❌ Decryption failed. Restored text does NOT match original.")
        print(f"(Expected: {original_plain_text})")

# --- 4. Starting Point (User Input) ---

# Clear screen (optional)
# print("\033[H\033[2J", end="")

# User must provide the results from the encryption script
plain_text_input = input("Enter the ORIGINAL plain message (for verification): ")
cipher_text_input = input("Enter the Ciphertext from the encryption process: ")
keys_input = input("Enter the Used Keys (list of integers, e.g., [1, 2, 3]): ")
base_input = input("Enter the Base Used (integer, e.g., 65 or 97): ")

# Convert inputs to correct types
try:
    used_keys_list = eval(keys_input)
    base_int = int(base_input)
    
    # Run the decryption algorithm
    main_decryption_run(cipher_text_input, used_keys_list, base_int, plain_text_input)
    
except NameError:
     print("\nERROR: Failed to convert 'Used Keys'. Make sure it is entered as a valid Python list (e.g., [1, 257, 4]).")
except ValueError:
     print("\nERROR: Failed to convert 'Base Used'. Make sure it is an integer.")
except Exception as e:
     print(f"\nAn unexpected error occurred during input parsing: {e}")