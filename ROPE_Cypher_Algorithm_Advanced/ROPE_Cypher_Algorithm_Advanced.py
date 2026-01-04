# import random
# import sys

# # Clear the console screen at startup (optional)
# print("\033[H\033[2J", end="")

# # --- 1. Key Generation Functions ---

# def generate_odd_key():
#     """Generates a random odd key between 1 and (2 ** 8)."""
#     return 2 * random.randint(1, (2 ** 8)) + 1

# def generate_even_key():
#     """Generates a random even key between 1 and (2 ** 8)."""
#     return 2 * random.randint(1, (2 ** 8))

# def generate_prime_key():
#     """Generates a random prime key between 2 and (2 ** 8)."""
#     while True:
#         p = random.randint(2, (2 ** 8)) 
#         # Primality check
#         is_prime = True
#         for i in range(2, int(p**0.5) + 1):
#             if p % i == 0:
#                 is_prime = False
#                 break
#         if is_prime:
#             return p

# # --- 2. Cipher and Decipher Helper Functions ---

# def get_base(char):
#     """Determines the base ASCII value ('A' or 'a') for a character."""
#     if char.isupper():
#         return ord('A')
#     elif char.islower():
#         return ord('a')
#     return None

# def encrypt_char(char, key):
#     """
#     Encrypts a single character. 
#     Cipher Equation: C = ((O - B) * K) + B
#     """
    
#     base = get_base(char)
    
#     if base is None:
#         # Return character as is for non-alphabetic chars
#         return char, ord(char), -128 
    
#     cipher_ord = ((ord(char) - base) * key) + base
    
#     return chr(cipher_ord), base, key

# def decrypt_char(cipher_char, base, key):
#     """
#     Decrypts a single character using the base and key.
#     Decipher Equation: O = ((C - B) / K) + B
#     """
    
#     cipher_value = ord(cipher_char)
    
#     # The result is cast to int as ASCII values are integers
#     original_ord_value = int(((cipher_value - base) / key) + base)
    
#     return chr(original_ord_value)

# def apply_alternating_cipher(plain_text):
#     """Applies the alternating cipher, returning the ciphertext, used keys, and the base."""
    
#     cipher_text = ""
#     used_keys = []
#     initial_base = 0 
#     key_generators = [generate_odd_key, generate_prime_key, generate_even_key]
    
#     for i, char in enumerate(plain_text):
#         if char == " ":
#             cipher_text += "?"
#             used_keys.append(-128) # Special key for space
#             continue
#         else:
#             # 1. Generate the alternating key
#             cipher_key = key_generators[i % 3]()
            
#             # 2. Encrypt
#             encrypted_char, base_used, key = encrypt_char(char, cipher_key)
            
#             # 3. Store result and key
#             cipher_text += encrypted_char
#             used_keys.append(key)
            
#             # 4. Store the base for decryption if this is the first alphabetic character
#             if initial_base == 0 and base_used not in [0, -128]:
#                 initial_base = base_used
                
#     return cipher_text, used_keys, initial_base

# # --- 3. Encryption Function ---

# def main_encryption_run(plain_text):
#     """Runs the full encryption process for the entire message."""
    
#     if not plain_text:
#         print("Input text cannot be empty.")
#         return None, None, None

#     # 1. Encrypt the text
#     final_cipher_text, used_keys, base = apply_alternating_cipher(plain_text)
    
#     # 2. Print Encryption Results (Crucial for decryption step)
#     print("\n" + "=" * 60)
#     print("--- 🔒 ENCRYPTION RESULTS (Part 1) 🔒 ---")
#     print(f"Original Text: {plain_text}")
#     print(f"Ciphertext:    {final_cipher_text}")
#     print(f"Used Keys:     {used_keys}")
#     print(f"Base Used:     {base} (e.g., ord('A')=65 or ord('a')=97)")
#     print("=" * 60 + "\n")
#     print(">>> NOTE: Please copy the 'Ciphertext', 'Used Keys', and 'Base Used' for the Decryption step below.")
    
#     return final_cipher_text, used_keys, base

# #--------------------------------------------------

# # --- 4. Decryption Function ---

# def main_decryption_run(cipher_text, used_keys, base, original_plain_text):
#     """Runs the full decryption process based on user inputs."""
    
#     if not cipher_text or not used_keys or base == 0:
#         print("\nERROR: Ciphertext, keys, and base are required for decryption.")
#         return

#     # 1. Decryption Process
#     decrypted_text = ""
#     cipher_text_index = 0
    
#     print("\n" + "=" * 60)
#     print("--- 🔓 DECRYPTION PROCESS (Part 2) 🔓 ---")
    
#     for i, key in enumerate(used_keys):
        
#         # Handle space character
#         if key == -128:
#             decrypted_text += " "
#             cipher_text_index += 1
#             continue
        
#         # Get the current ciphertext character
#         cipher_char = cipher_text[cipher_text_index]
        
#         # Determine the correct base for the current character being decrypted.
#         # This uses a simple case check on the cipher_char, assuming the key transforms case-sensitively.
#         if cipher_char.isupper():
#              current_base = ord('A')
#         elif cipher_char.islower():
#              current_base = ord('a')
#         else:
#              current_base = base # Fallback to the initial base

#         # Decrypt
#         try:
#             decrypted_char = decrypt_char(cipher_char, current_base, key)
#             decrypted_text += decrypted_char
#         except Exception as e:
#             decrypted_text += "[ERR]"
#             print(f"Error decrypting char '{cipher_char}' with key {key}: {e}")
            
#         cipher_text_index += 1
        
#     print(f"\nRestored Text: {decrypted_text}")
#     print("=" * 60)

#     # 2. Verification
#     if decrypted_text == original_plain_text:
#         print("✅ Verification successful. Restored text matches original.")
#     else:
#         print("❌ Verification failed. Restored text does NOT match original.")
#         print(f"(Expected: {original_plain_text})")

# # --- 5. Main Control Flow ---

# def main():
    
#     # 1. ENCRYPTION PHASE
#     print("\n*** Phase 1: Encryption ***")
#     user_input = input("Please enter the message to encrypt: ")
    
#     final_cipher_text, used_keys, base = main_encryption_run(user_input)

#     if final_cipher_text is None:
#         return

#     # 2. DECRYPTION PHASE (Interactive)
    
#     print("\n*** Phase 2: Decryption Input ***")
    
#     # We ask for the inputs again to simulate the separation between sender/receiver
#     plain_text_verify = input("Enter the ORIGINAL plain message again (for final verification): ")
#     cipher_text_decrypt = input("Enter the Ciphertext copied from above: ")
#     keys_decrypt = input("Enter the Used Keys (list of integers, e.g., [1, 257, 4]): ")
#     base_decrypt = input("Enter the Base Used (integer, e.g., 65 or 97): ")
    
#     # Convert inputs to correct types
#     try:
#         used_keys_list = eval(keys_decrypt)
#         base_int = int(base_decrypt)
        
#         # Run the decryption algorithm
#         main_decryption_run(cipher_text_decrypt, used_keys_list, base_int, plain_text_verify)
        
#     except NameError:
#          print("\nERROR: Failed to convert 'Used Keys'. Make sure it is entered as a valid Python list (e.g., [1, 257, 4]).")
#     except ValueError:
#          print("\nERROR: Failed to convert 'Base Used'. Make sure it is an integer.")
#     except Exception as e:
#          print(f"\nAn unexpected error occurred during input parsing: {e}")

# if __name__ == "__main__":
#     main()

# =======================================================================================================================================================

# import random
# import sys
# import os # Import the os module for path handling (optional but good practice)

# # ====================================================================
# # !!! 🛑 YOU MUST CHANGE THIS PATH TO YOUR DESIRED LOCATION 🛑 !!!
# # Example for Windows: "C:\\Users\\YourUser\\Desktop\\cipher_output.txt"
# # Example for Linux/macOS: "/Users/YourUser/Documents/cipher_output.txt"
# OUTPUT_FILE_PATH = "E:\\cipher_output.txt" 
# # ====================================================================

# # Clear the console screen at startup (optional)
# print("\033[H\033[2J", end="")

# # --- 1. Key Generation Functions ---

# def generate_odd_key():
#     """Generates a random odd key between 1 and (2 ** 8)."""
#     return 2 * random.randint(1, (2 ** 8)) + 1

# def generate_even_key():
#     """Generates a random even key between 1 and (2 ** 8)."""
#     return 2 * random.randint(1, (2 ** 8))

# def generate_prime_key():
#     """Generates a random prime key between 2 and (2 ** 8)."""
#     while True:
#         p = random.randint(2, (2 ** 8)) 
#         # Primality check
#         is_prime = True
#         for i in range(2, int(p**0.5) + 1):
#             if p % i == 0:
#                 is_prime = False
#                 break
#         if is_prime:
#             return p

# # --- 2. Cipher and Decipher Helper Functions ---

# def get_base(char):
#     """Determines the base ASCII value ('A' or 'a') for a character."""
#     if char.isupper():
#         return ord('A')
#     elif char.islower():
#         return ord('a')
#     return None

# def encrypt_char(char, key):
#     """
#     Encrypts a single character. 
#     Cipher Equation: C = ((O - B) * K) + B
#     """
    
#     base = get_base(char)
    
#     if base is None:
#         return char, ord(char), -128 
    
#     cipher_ord = ((ord(char) - base) * key) + base
    
#     return chr(cipher_ord), base, key

# def decrypt_char(cipher_char, base, key):
#     """
#     Decrypts a single character using the base and key.
#     Decipher Equation: O = ((C - B) / K) + B
#     """
    
#     cipher_value = ord(cipher_char)
#     original_ord_value = int(((cipher_value - base) / key) + base)
    
#     return chr(original_ord_value)

# def apply_alternating_cipher(plain_text):
#     """Applies the alternating cipher, returning the ciphertext, used keys, and the base."""
    
#     cipher_text = ""
#     used_keys = []
#     initial_base = 0 
#     key_generators = [generate_odd_key, generate_prime_key, generate_even_key]
    
#     for i, char in enumerate(plain_text):
#         if char == " ":
#             cipher_text += "?"
#             used_keys.append(-128) # Special key for space
#             continue
#         else:
#             cipher_key = key_generators[i % 3]()
#             encrypted_char, base_used, key = encrypt_char(char, cipher_key)
            
#             cipher_text += encrypted_char
#             used_keys.append(key)
            
#             if initial_base == 0 and base_used not in [0, -128]:
#                 initial_base = base_used
                
#     return cipher_text, used_keys, initial_base

# # --- 3. File Saving Function ---

# def save_encryption_data(file_path, plain_text, cipher_text, used_keys, base):
#     """Saves the encryption data to a specified text file."""
#     try:
#         with open(file_path, 'w', encoding='utf-8') as f:
#             f.write("--- Cipher Output Data ---\n")
#             f.write(f"Original Text: {plain_text}\n")
#             f.write("-" * 30 + "\n")
#             f.write("Data Required for Decryption:\n")
#             f.write(f"1. Ciphertext: {cipher_text}\n")
#             f.write(f"2. Used Keys (Python List Format): {used_keys}\n")
#             f.write(f"3. Base Used (Integer): {base}\n")
#             f.write("-" * 30 + "\n")
#             print(f"\n✅ Data successfully saved to: {os.path.abspath(file_path)}")
            
#     except IOError as e:
#         print(f"\n❌ ERROR: Could not write to file at path '{file_path}'. Check your file permissions or the path itself.")
#         print(f"Details: {e}")
        
#     except Exception as e:
#         print(f"\n❌ An unexpected error occurred during file saving: {e}")


# # --- 4. Encryption Function (Modified to Save) ---

# def main_encryption_run(plain_text):
#     """Runs the full encryption process and saves the results."""
    
#     if not plain_text:
#         print("Input text cannot be empty.")
#         return None, None, None

#     # 1. Encrypt the text
#     final_cipher_text, used_keys, base = apply_alternating_cipher(plain_text)
    
#     # 2. Print Encryption Results
#     print("\n" + "=" * 60)
#     print("--- 🔒 ENCRYPTION RESULTS (Part 1) 🔒 ---")
#     print(f"Original Text: {plain_text}")
#     print(f"Ciphertext:    {final_cipher_text}")
#     print(f"Used Keys:     {used_keys}")
#     print(f"Base Used:     {base}")
#     print("=" * 60 + "\n")

#     # 3. Save the results to the file
#     save_encryption_data(OUTPUT_FILE_PATH, plain_text, final_cipher_text, used_keys, base)

#     return final_cipher_text, used_keys, base

# #--------------------------------------------------

# # --- 5. Decryption Function (Unchanged, uses interactive input) ---

# def main_decryption_run(cipher_text, used_keys, base, original_plain_text):
#     """Runs the full decryption process based on user inputs."""
    
#     if not cipher_text or not used_keys or base == 0:
#         print("\nERROR: Ciphertext, keys, and base are required for decryption.")
#         return

#     # 1. Decryption Process
#     decrypted_text = ""
#     cipher_text_index = 0
    
#     print("\n" + "=" * 60)
#     print("--- 🔓 DECRYPTION PROCESS (Part 2) 🔓 ---")
    
#     for i, key in enumerate(used_keys):
        
#         if key == -128:
#             decrypted_text += " "
#             cipher_text_index += 1
#             continue
        
#         cipher_char = cipher_text[cipher_text_index]
        
#         # Determine base based on character case
#         if cipher_char.isupper():
#              current_base = ord('A')
#         elif cipher_char.islower():
#              current_base = ord('a')
#         else:
#              current_base = base 

#         # Decrypt
#         try:
#             decrypted_char = decrypt_char(cipher_char, current_base, key)
#             decrypted_text += decrypted_char
#         except Exception as e:
#             decrypted_text += "[ERR]"
#             print(f"Error decrypting char '{cipher_char}' with key {key}: {e}")
            
#         cipher_text_index += 1
        
#     print(f"\nRestored Text: {decrypted_text}")
#     print("=" * 60)

#     # 2. Verification
#     if decrypted_text == original_plain_text:
#         print("✅ Verification successful. Restored text matches original.")
#     else:
#         print("❌ Verification failed. Restored text does NOT match original.")
#         print(f"(Expected: {original_plain_text})")

# # --- 6. Main Control Flow ---

# def main():
    
#     # 1. ENCRYPTION PHASE
#     print("\n*** Phase 1: Encryption ***")
#     user_input = input("Please enter the message to encrypt: ")
    
#     final_cipher_text, used_keys, base = main_encryption_run(user_input)

#     if final_cipher_text is None:
#         return

#     # 2. DECRYPTION PHASE (Interactive)
    
#     print("\n*** Phase 2: Decryption Input ***")
#     print(">>> You can now use the data saved in the output file for the following inputs.")
    
#     plain_text_verify = input("Enter the ORIGINAL plain message again (for final verification): ")
#     cipher_text_decrypt = input("Enter the Ciphertext copied from the file: ")
#     keys_decrypt = input("Enter the Used Keys (list of integers, e.g., [1, 257, 4]) copied from the file: ")
#     base_decrypt = input("Enter the Base Used (integer, e.g., 65 or 97) copied from the file: ")
    
#     # Convert inputs to correct types
#     try:
#         used_keys_list = eval(keys_decrypt)
#         base_int = int(base_decrypt)
        
#         # Run the decryption algorithm
#         main_decryption_run(cipher_text_decrypt, used_keys_list, base_int, plain_text_verify)
        
#     except NameError:
#          print("\nERROR: Failed to convert 'Used Keys'. Make sure it is entered as a valid Python list (e.g., [1, 257, 4]).")
#     except ValueError:
#          print("\nERROR: Failed to convert 'Base Used'. Make sure it is an integer.")
#     except Exception as e:
#          print(f"\nAn unexpected error occurred during input parsing: {e}")

# if __name__ == "__main__":
#     main()

#=================================================================================================================================================================

# import random
# import sys

# # Clear the console screen at startup (optional)
# print("\033[H\033[2J", end="")

# # --- 1. Key Generation Functions ---
# # (Keys can range up to 513)

# def generate_odd_key():
#     """Generates a random odd key between 1 and (2 ** 8)."""
#     return 2 * random.randint(1, (2 ** 8)) + 1

# def generate_even_key():
#     """Generates a random even key between 1 and (2 ** 8)."""
#     return 2 * random.randint(1, (2 ** 8))

# def generate_prime_key():
#     """Generates a random prime key between 2 and (2 ** 8)."""
#     while True:
#         p = random.randint(2, (2 ** 8)) 
#         # Primality check
#         is_prime = True
#         for i in range(2, int(p**0.5) + 1):
#             if p % i == 0:
#                 is_prime = False
#                 break
#         if is_prime:
#             return p

# # --- 2. Cipher and Decipher Helper Functions ---

# def get_base(char):
#     """Determines the base ASCII value ('A' or 'a') for a character."""
#     if char.isupper():
#         return ord('A')
#     elif char.islower():
#         return ord('a')
#     return None

# def encrypt_char(char, key):
#     """
#     Encrypts a single character. 
#     Cipher Equation: C = ((O - B) * K) + B
#     """
    
#     base = get_base(char)
    
#     if base is None:
#         return char, ord(char), -128 
    
#     cipher_ord = ((ord(char) - base) * key) + base
    
#     return chr(cipher_ord), base, key

# def decrypt_char(cipher_char, base, key):
#     """
#     Decrypts a single character using the base and key.
#     Decipher Equation: O = ((C - B) / K) + B
#     """
    
#     cipher_value = ord(cipher_char)
#     # Note: We must ensure K is not 0, which is handled by key generation.
#     original_ord_value = int(((cipher_value - base) / key) + base)
    
#     return chr(original_ord_value)

# def apply_alternating_cipher(plain_text):
#     """Applies the alternating cipher, returning the ciphertext, used keys, and the base."""
    
#     cipher_text = ""
#     used_keys = []
#     initial_base = 0 
#     key_generators = [generate_odd_key, generate_prime_key, generate_even_key]
    
#     for i, char in enumerate(plain_text):
#         if char == " ":
#             cipher_text += "?"
#             used_keys.append(-128) # Special key for space
#             continue
#         else:
#             # 1. Generate the alternating key
#             cipher_key = key_generators[i % 3]()
            
#             # 2. Encrypt
#             encrypted_char, base_used, key = encrypt_char(char, cipher_key)
            
#             # 3. Store result and key
#             cipher_text += encrypted_char
#             used_keys.append(key)
            
#             # 4. Store the base for decryption
#             if initial_base == 0 and base_used not in [0, -128]:
#                 initial_base = base_used
                
#     return cipher_text, used_keys, initial_base

# # --- 3. Encryption Function (Modified to embed keys) ---

# def main_encryption_run(plain_text):
#     """Runs the full encryption process and embeds the keys into the ciphertext."""
    
#     if not plain_text:
#         print("Input text cannot be empty.")
#         return None, None, None

#     # 1. Encrypt the text
#     cipher_text_core, used_keys, base = apply_alternating_cipher(plain_text)
    
#     # 2. Convert keys (integers) to chars and append to ciphertext
#     # We must ensure the key value fits within a representable char range. 
#     # Since keys can exceed 255 (e.g., 513), we must handle keys over 255 
#     # by using a safe modulo or by checking the max key value allowed.
#     # Given the max key is 513, we will use two chars for keys > 255.
    
#     keys_as_chars = ""
#     safe_keys_used = [] # Store keys in a format that fits 1 or 2 characters
    
#     # The max key is 2*256 + 1 = 513. We use two bytes for keys > 255.
    
#     for key in used_keys:
#         if key == -128:
#             # -128 represents a space, we can map it to a specific single char 
#             # (e.g., ASCII 255, which is often unused)
#             keys_as_chars += chr(255) 
#             safe_keys_used.append(255)
#         elif key <= 255:
#             # Fits in one character (0-255)
#             keys_as_chars += chr(key)
#             safe_keys_used.append(key)
#         else:
#             # Key > 255 (Max 513). We cannot reliably embed it as a single char (bytes)
#             # We will use two characters to encode: key = c1*256 + c2
#             # For simplicity and robustness given the code's structure, 
#             # we will print the keys as a list and use the original method 
#             # for decryption *unless* we constrain keys to be <= 255.
            
#             # Reverting to the original structure for keys > 255 is necessary 
#             # without a complex encoding scheme. We'll constrain the keys 
#             # to fit max 255 for the *safe embedding* part.
            
#             # For this exercise, since the max key is 513, we will use a simplified 
#             # ASCII embedding that only works for keys <= 255, and fail gracefully 
#             # if a larger key appears, or simply use the remainder, which is lossy.
            
#             # **To fulfill the user request:** we will use modulo 255, which is LOSSY but embeds.
#             # A correct approach requires two chars per large key, or strict key size limits.
            
#             # Let's use the actual key value directly and assume the decoder can handle the range.
#             # Python's chr() can handle values > 255, but the resulting character 
#             # might not be correctly retrieved via ord() in all environments (lossy conversion).
#             # For simplicity in this demo, we'll map the key into the range 32-254 (printable extended ASCII).
            
#             mapped_key = key % 223 + 32 # Maps key to a printable range (32 to 254)
#             keys_as_chars += chr(mapped_key)
#             safe_keys_used.append(mapped_key)

#     # 3. Final Ciphertext
#     final_cipher_text_with_keys = cipher_text_core + keys_as_chars
    
#     # 4. Print Encryption Results
#     print("\n" + "=" * 60)
#     print("--- 🔒 ENCRYPTION RESULTS (Part 1) 🔒 ---")
#     print(f"Original Text Length: {len(plain_text)}")
#     print(f"Final Ciphertext (Core + Keys): {final_cipher_text_with_keys}")
#     print(f"Base Used: {base}")
#     print("=" * 60 + "\n")
#     print(">>> NOTE: Decryption needs the full Ciphertext and the Original Length for separation.")
    
#     return final_cipher_text_with_keys, len(plain_text), base

# #--------------------------------------------------

# # --- 5. Decryption Function (Modified to use single input) ---

# def main_decryption_run(full_cipher_text, original_length_input, base):
#     """
#     Runs the full decryption process by extracting keys from the ciphertext.
#     Requires: The full ciphertext (core + keys), the original text length, and the Base.
#     """
    
#     try:
#         original_length = int(original_length_input)
#         base_int = int(base)
#     except ValueError:
#         print("\nERROR: Original length and Base must be valid integers.")
#         return

#     # 1. Separate Ciphertext and Keys
#     cipher_text_core = full_cipher_text[:original_length]
#     keys_as_chars = full_cipher_text[original_length:]
    
#     if len(cipher_text_core) != original_length or len(keys_as_chars) != original_length:
#         print("\nERROR: Length mismatch. Check the original length input and the ciphertext structure.")
#         return
        
#     # 2. Reconstruct Keys from Chars
#     used_keys = []
    
#     for char in keys_as_chars:
#         key_value = ord(char)
        
#         # Reverse the mapping used in encryption
#         if key_value == 255:
#             # This was the space key (-128)
#             used_keys.append(-128)
#         else:
#             # Reverse the modulo mapping (lossy, but follows the encryption logic)
#             # Key = mapped_key - 32 + n*223. Since we don't have 'n', this is inaccurate.
#             # *For a working demo, we use the character value directly, assuming the mapping is sufficient.*
#             key_value_unmapped = key_value # Using the character's ASCII value as the key
#             used_keys.append(key_value_unmapped)
    
#     # 3. Decryption Process
#     decrypted_text = ""
#     cipher_text_index = 0
    
#     print("\n" + "=" * 60)
#     print("--- 🔓 DECRYPTION PROCESS (Part 2) 🔓 ---")
    
#     for i, key in enumerate(used_keys):
        
#         # Handle space key (-128)
#         if key == -128:
#             decrypted_text += " "
#             cipher_text_index += 1
#             continue
        
#         cipher_char = cipher_text_core[cipher_text_index]
        
#         # Determine base based on character case
#         if cipher_char.isupper():
#              current_base = ord('A')
#         elif cipher_char.islower():
#              current_base = ord('a')
#         else:
#              current_base = base_int # Fallback

#         # Decrypt
#         try:
#             # Note: The key used here is the *mapped* key, which is INCORRECT 
#             # if the original key was > 255. Decryption will fail unless 
#             # all generated keys were <= 255 (which is not guaranteed).
#             decrypted_char = decrypt_char(cipher_char, current_base, key)
#             decrypted_text += decrypted_char
#         except Exception as e:
#             decrypted_text += "[ERR]"
#             print(f"Error decrypting char '{cipher_char}' with key {key}: {e}")
            
#         cipher_text_index += 1
        
#     print(f"\nRestored Text: {decrypted_text}")
#     print("=" * 60)

# # --- 6. Main Control Flow ---

# def main():
    
#     # 1. ENCRYPTION PHASE
#     print("\n*** Phase 1: Encryption ***")
#     user_input = input("Please enter the message to encrypt: ")
    
#     final_cipher_text_with_keys, original_length, base = main_encryption_run(user_input)

#     if final_cipher_text_with_keys is None:
#         return

#     # 2. DECRYPTION PHASE (Modified for single input)
    
#     print("\n*** Phase 2: Decryption Input ***")
    
#     # Ask for the required components for decryption
#     cipher_text_decrypt = input("Enter the FULL Ciphertext (Core + Keys) copied from above: ")
    
#     # We still need the base and original length to correctly separate the components
#     length_input = input("Enter the ORIGINAL Text Length (from above): ")
#     base_input = input("Enter the Base Used (integer, e.g., 65 or 97) from above: ")
    
#     # Run the decryption algorithm
#     main_decryption_run(cipher_text_decrypt, length_input, base_input)

# if __name__ == "__main__":
#     main()

#--------------------------------------------------------------------------------------------------------------------------------------------

import random
import sys

# Clear the console screen at startup (optional)
print("\033[H\033[2J", end="")

# --- Key Encoding/Decoding Map (Base 62-like) ---
# Used to encode large integer keys into a string containing only letters and digits.
KEY_MAP = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
KEY_BASE = len(KEY_MAP)

def encode_key_to_string(number):
    """Converts a large integer key into a Base62-like string."""
    if number == 0:
        return KEY_MAP[0]
    is_negative = number < 0
    number = abs(number)
    
    encoded = ""
    while number > 0:
        encoded = KEY_MAP[number % KEY_BASE] + encoded
        number //= KEY_BASE
        
    return '-' + encoded if is_negative else encoded

def decode_string_to_key(encoded_string):
    """Converts a Base62-like string back into the original integer key."""
    if not encoded_string:
        return 0
    
    is_negative = encoded_string[0] == '-'
    if is_negative:
        encoded_string = encoded_string[1:]
        
    number = 0
    for char in encoded_string:
        try:
            digit = KEY_MAP.index(char)
            number = number * KEY_BASE + digit
        except ValueError:
             # Should not happen if encoding is correct, but safe check
             print(f"Error: Invalid character in encoded key: {char}")
             return 0 # Return 0 or raise error
             
    return -number if is_negative else number

# --- 1. Key Generation Functions (Unchanged) ---

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

# --- 2. Cipher and Decipher Helper Functions (Unchanged) ---

def get_base(char):
    """Determines the base ASCII value ('A' or 'a') for a character."""
    if char.isupper():
        return ord('A')
    elif char.islower():
        return ord('a')
    return None

def encrypt_char(char, key):
    """
    Encrypts a single character. 
    Cipher Equation: C = ((O - B) * K) + B
    """
    base = get_base(char)
    if base is None:
        return char, ord(char), -128 
    
    cipher_ord = ((ord(char) - base) * key) + base
    return chr(cipher_ord), base, key

def decrypt_char(cipher_char, base, key):
    """
    Decrypts a single character using the base and key.
    Decipher Equation: O = ((C - B) / K) + B
    """
    cipher_value = ord(cipher_char)
    original_ord_value = int(((cipher_value - base) / key) + base)
    return chr(original_ord_value)

def apply_alternating_cipher(plain_text):
    """Applies the alternating cipher, returning the ciphertext, used keys, and the base."""
    
    cipher_text = ""
    used_keys = []
    initial_base = 0 
    key_generators = [generate_odd_key, generate_prime_key, generate_even_key]
    
    for i, char in enumerate(plain_text):
        if char == " ":
            cipher_text += "?"
            used_keys.append(-128) # Special key for space
            continue
        else:
            cipher_key = key_generators[i % 3]()
            encrypted_char, base_used, key = encrypt_char(char, cipher_key)
            
            cipher_text += encrypted_char
            used_keys.append(key)
            
            if initial_base == 0 and base_used not in [0, -128]:
                initial_base = base_used
                
    return cipher_text, used_keys, initial_base

# --- 3. Encryption Function (Modified to embed keys) ---

def main_encryption_run(plain_text):
    """Runs the full encryption process and embeds the keys into the final ciphertext."""
    
    if not plain_text:
        print("Input text cannot be empty.")
        return None, None, None

    # 1. Encrypt the text
    final_cipher_text, used_keys, base = apply_alternating_cipher(plain_text)
    
    # 2. Encode Keys and Base into a single string
    
    # Append the initial base to the keys list for encoding
    keys_and_base = used_keys + [base] 
    
    encoded_keys = ""
    for key in keys_and_base:
        encoded_keys += encode_key_to_string(key) + '$'
    
    # Remove the trailing '$'
    encoded_keys = encoded_keys.rstrip('$') 
    
    # 3. Create Final Transmitted Text
    # Format: [Ciphertext][#][Encoded Keys and Base]
    transmitted_text = f"{final_cipher_text}#{encoded_keys}"
    
    # 4. Print Encryption Results
    print("\n" + "=" * 80)
    print("--- 🔒 ENCRYPTION RESULTS (Part 1) 🔒 ---")
    print(f"Original Text: {plain_text}")
    print(f"Ciphertext (raw): {final_cipher_text}")
    print(f"Used Keys (raw): {used_keys}")
    print(f"Base Used (raw): {base}")
    print("-" * 80)
    print(f"✅ FINAL TRANSMITTED CIPHERTEXT (Input for Decryption):\n{transmitted_text}")
    print("=" * 80 + "\n")
    
    return transmitted_text, used_keys, base

#--------------------------------------------------

# --- 4. Decryption Function (Modified to parse embedded keys) ---

def main_decryption_run(transmitted_text):
    """Runs the full decryption process, extracting keys from the transmitted text."""
    
    if '#' not in transmitted_text:
        print("\nERROR: Invalid ciphertext format. Missing separator ('#').")
        return

    # 1. Split Text to get Ciphertext and Encoded Keys
    parts = transmitted_text.split('#', 1)
    if len(parts) != 2:
        print("\nERROR: Failed to separate ciphertext and keys.")
        return
        
    cipher_text = parts[0]
    encoded_keys_string = parts[1]
    
    # 2. Decode Keys and Base
    encoded_keys_list = encoded_keys_string.split('$')
    
    decoded_keys_and_base = []
    try:
        for encoded_key in encoded_keys_list:
            decoded_keys_and_base.append(decode_string_to_key(encoded_key))
    except Exception as e:
        print(f"\nERROR: Failed to decode keys from string: {e}")
        return

    # Extract the base and the actual keys
    base = decoded_keys_and_base[-1]
    used_keys = decoded_keys_and_base[:-1]
    
    if not cipher_text or not used_keys or base == 0:
        print("\nERROR: Extracted keys or base are invalid.")
        return

    # 3. Decryption Process
    decrypted_text = ""
    cipher_text_index = 0
    
    print("\n" + "=" * 80)
    print("--- 🔓 DECRYPTION PROCESS (Part 2) 🔓 ---")
    print(f"Extracted Ciphertext: {cipher_text}")
    print(f"Extracted Keys:      {used_keys}")
    print(f"Extracted Base:      {base}")
    print("-" * 80)
    
    for i, key in enumerate(used_keys):
        
        # Handle space character
        if key == -128:
            decrypted_text += " "
            cipher_text_index += 1
            continue
        
        # Get the current ciphertext character
        cipher_char = cipher_text[cipher_text_index]
        
        # Determine the correct base for the current character being decrypted.
        if cipher_char.isupper():
             current_base = ord('A')
        elif cipher_char.islower():
             current_base = ord('a')
        else:
             current_base = base # Fallback to the initial base

        # Decrypt
        try:
            decrypted_char = decrypt_char(cipher_char, current_base, key)
            decrypted_text += decrypted_char
        except Exception as e:
            decrypted_text += "[ERR]"
            print(f"Error decrypting char '{cipher_char}' with key {key}: {e}")
            
        cipher_text_index += 1
        
    print(f"\nRestored Text: {decrypted_text}")
    print("=" * 80)

# --- 5. Main Control Flow ---

def main():
    
    # 1. ENCRYPTION PHASE
    print("\n*** Phase 1: Encryption ***")
    user_input = input("Please enter the message to encrypt: ")
    
    transmitted_text, _, _ = main_encryption_run(user_input)

    if transmitted_text is None:
        return

    # 2. DECRYPTION PHASE (Interactive)
    
    print("\n*** Phase 2: Decryption Input ***")
    
    # Only ONE input is required now!
    cipher_txt_input = input("Enter the FULL Ciphertext (including the keys, e.g., '...#EncodedKeys'): ")
    
    # Run the decryption algorithm
    main_decryption_run(cipher_txt_input)

if __name__ == "__main__":
    main()