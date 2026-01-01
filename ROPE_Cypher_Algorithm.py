# # Clear screen using ANSI escape codes
# print("\033[H\033[2J", end="")

# # import libraries:
# import random

# # Numbers Generating functions:
# # ODD
# def odd():
#     return 2 * random.randint(1, (2 ** 127) - 1) + 1

# # PRIME
# def prime():
#     while True:
#         rpn = random.randint(2, (2 ** 128))
#         is_prime = True
#         for i in range(2, int(rpn**0.5) + 1):
#             if rpn % i == 0:
#                 is_prime = False
#                 break
#         if is_prime:
#             return rpn

# # EVEN
# def even():
#     return 2 * random.randint(1, (2 ** 127))

# # Decleration needed inputs, variables:
# # plaTxt = input("Enter your text: ")
# CipTxt = ""
# SecKey = []
# plaTxt = "RIYADH # 123 $ riyadh"

# # Getting inserted Txt Length & Divide it by 3:
# txtLen = len(plaTxt)
# txtDivBy3 =  len(plaTxt) // 3
# txtReminder = len(plaTxt) % 3

# # Aplying The Algorithm
# def encrypt_char(char, key):
#     if char.isupper():
#         base = ord('A')
#     elif char.islower():
#         base = ord('a')
#     else:
#         return '!'

    # char_index = ord(char) - base
    # cipher_index = (char_index * key) % 26
    # return chr(cipher_index + base)

# for i, n in enumerate(plaTxt):
# for i, n in txtLen, plaTxt:
#     if i == 0:
#         cipher_key = odd()
#         CipTxt += encrypt_char(n, cipher_key)
#     elif i == 1:
#         cipher_key = prime()
#         CipTxt += encrypt_char(n, cipher_key)
#     elif i == 2:
#         cipher_key = even()
#         CipTxt += encrypt_char(n, cipher_key)

# print(CipTxt)

# ==================================================================================================

# # Aplaying The Cipher
# for i in plaTxt:
#     CipTxt += encrypt_char(i, cipher_key)

# for i in plaTxt:
#     CipTxt += encrypt_char(i, cipher_key)



# print(f"Last character: {text[length - 1]}")

# ==================================================================================================

# # Clear screen using ANSI escape codes
# print("\033[H\033[2J", end="")

# # import libraries:
# import random

# # --- Numbers Generating functions (Optimized) ---
# def odd():
#     """تولد رقماً فردياً عشوائياً كبيراً."""
#     # يفضل استخدام نطاق أصغر للمفاتيح (مثل 1 إلى 255) في التشفير العملي لتجنب تجاوزات القيم
#     return 2 * random.randint(1, 1000) + 1

# def even():
#     """تولد رقماً زوجياً عشوائياً كبيراً."""
#     return 2 * random.randint(1, 1000)

# def prime():
#     """تولد رقماً أولياً عشوائياً (نطاق أصغر للكفاءة)."""
#     # نطاق أصغر (2-1000) يضمن العثور على أولي بسرعة أكبر
#     while True:
#         rpn = random.randint(2, 1000)
#         is_prime = True
#         for i in range(2, int(rpn**0.5) + 1):
#             if rpn % i == 0:
#                 is_prime = False
#                 break
#         if is_prime:
#             return rpn

# # --- دالة التشفير الرياضي ---
# def encrypt_char(char, key):
#     """تشفير حرف واحد باستخدام مفتاح الضرب Modulo 26."""
#     if char.isupper():
#         base = ord('A')
#     elif char.islower():
#         base = ord('a')
#     else:
#         return char # حافظ على الأرقام والرموز بدلاً من استبدالها بـ '!'

#     char_index = ord(char) - base
#     # (المؤشر الأصلي * المفتاح) % 26
#     cipher_index = (char_index * key) % 26
#     return chr(cipher_index + base)

# # --- الجزء الرئيسي لتطبيق الخوارزمية ---

# CipTxt = ""
# plaTxt = "RIYADH # 123 $ riyadh"

# # قائمة المفاتيح الثلاثة
# key_generators = [odd, prime, even] # يمكن الوصول إليها عبر المؤشر 0, 1, 2

# # Aplying The Algorithm
# # نستخدم enumerate للحصول على المؤشر i والحرف n في نفس الوقت.
# for i, n in enumerate(plaTxt):
    
#     # تحديد مفتاح التشفير بناءً على دورة (0، 1، 2، 0، 1، 2، ...)
#     # معامل الباقي i % 3 يضمن أن يكون المؤشر دائماً 0 أو 1 أو 2.
#     key_index = i % 3
    
#     # 1. توليد المفتاح: نختار الدالة (odd أو prime أو even) بناءً على key_index، ثم نستدعيها.
#     # يتم توليد مفتاح جديد لكل حرف!
#     cipher_key = key_generators[key_index]()

#     # 2. التشفير
#     CipTxt += encrypt_char(n, cipher_key)

# # Printing Ciphered Txt
# print(f"النص الأصلي: {plaTxt}")
# print(f"النص المشفر: {CipTxt}")

#===================================================================================================

# # Clear screen using ANSI escape codes
# print("\033[H\033[2J", end="")

# # import libraries:
# import random

# def odd():
#     return 2 * random.randint(1, (2 ** 32)) + 1

# def prime():
#     while True:
#         rpn = random.randint(2, (2 ** 32))
#         is_prime = True

#         for i in range(2, int(rpn**0.5) + 1):
#             if rpn % i == 0:
#                 is_prime = False
#                 break
        
#         if is_prime:
#             return rpn

# def even():
#     return 2 * random.randint(1, (2 ** 32))

# Sec_Key = []

# def encrypt_char(char, key):
    

#     """Encrypting a single character using the Modulo 26 multiplication key."""
#     if char.isupper():
#         base = ord('A')
#     elif char.islower():
#         base = ord('a')
#     else:
#         return char

#     char_index = ord(char) - base
    
#     cipher_index = (char_index * key) % 26
    
#     return chr(cipher_index + base)

# def apply_alternating_cipher(plaTxt):
#     """
#     Apply alternating encoding (Odd, Prime, Even) to the text.
#     Divide the length of the text by 3.
#     """
#     CipTxt = ""
    
#     key_generators = [odd, prime, even] 

#     for i, n in enumerate(plaTxt):
        
#         cipher_key = key_generators[i % 3]()
#         Sec_Key.append(cipher_key)

#         CipTxt += encrypt_char(n, cipher_key)

#     txtLen = len(plaTxt)
#     txtDivBy3 = txtLen // 3
#     txtReminder = txtLen % 3

#     print(f"--- analysing text ---")
#     print(f"txt len: {txtLen}")
#     print(f"result of a correct division by 3: {txtDivBy3}")
#     print(f"Rest: {txtReminder}")
#     print(f"orginal txt: {plaTxt}")
#     print("-" * 30)

#     return CipTxt

# plaTxt = "Bella"

# final_cipher_text = apply_alternating_cipher(plaTxt)

# print(Sec_Key)

# print(f"cipher txt result: {final_cipher_text}")

# # decryption..........................................



# اختيار المفتاح يعتمد فقط على أول 3 أحرف، ولا يوجد تكرار دوري

# لا يوجد أي ضمان أن المفتاح صالح رياضيًا (gcd(key, 26) = 1) 


#===================================================================================================

# Clear screen using ANSI escape codes
print("\033[H\033[2J", end="")

# import libraries:
import random
import math # نحتاج إلى math.gcd لحساب القاسم المشترك الأكبر

# --- دوال توليد الأرقام (مع تعديل بسيط لضمان كفاءة Prime) ---

def odd():
    """تولد رقماً فردياً عشوائياً."""
    # لا يزال المفتاح الناتج قد يكون غير قابل للعكس Mod 26، لكننا نعتمد على أن يكون المفتاح نفسه فردي.
    return 2 * random.randint(1, (2 ** 32)) + 1

def even():
    """تولد رقماً زوجياً عشوائياً."""
    return 2 * random.randint(1, (2 ** 32))

def prime():
    """تولد رقماً أولياً عشوائياً (نطاق أصغر للكفاءة)."""
    # نطاق أصغر لضمان العثور على أولي بسرعة
    while True:
        rpn = random.randint(2, (2 ** 32)) 
        is_prime = True
        
        for i in range(2, int(rpn**0.5) + 1):
            if rpn % i == 0:
                is_prime = False
                break
        
        if is_prime:
            return rpn

# --- التشفير (Encryption) ---
Sec_Key = []

def encrypt_char(char, key):
    """تشفير حرف واحد باستخدام مفتاح الضرب Modulo 26."""
    if char.isupper():
        base = ord('A')
    elif char.islower():
        base = ord('a')
    else:
        return char

    # ****************** خطوة التأكد من صلاحية المفتاح ******************
    # يجب أن نضمن أن المفتاح الفعلي المستخدم في التشفير (key % 26) صالح.
    # بما أننا نستخدم Key كبير، فإن المفتاح الفعلي هو K_mod_26
    K_mod_26 = key % 26
    
    # إذا كان المفتاح غير صالح (زوجي أو يقبل القسمة على 13)
    if math.gcd(K_mod_26, 26) != 1:
        # لغرض التشفير، سنستخدم المفتاح 1 (أو مفتاح صالح آخر) بدلاً من المفتاح غير الصالح.
        K_mod_26 = 1 
        
    # نعيد تخزين المفتاح الصحيح الذي تم استخدامه في قائمة المفاتيح
    Sec_Key.append(K_mod_26)

    char_index = ord(char) - base
    cipher_index = (char_index * K_mod_26) % 26
    
    return chr(cipher_index + base)

def apply_alternating_cipher(plaTxt):
    """
    تطبيق التشفير المتناوب (Odd, Prime, Even) على النص.
    """
    CipTxt = ""
    key_generators = [odd, prime, even] 

    # تفريغ قائمة المفاتيح قبل البدء في التشفير الجديد
    Sec_Key.clear() 

    for i, n in enumerate(plaTxt):
        cipher_key_large = key_generators[i % 3]()
        
        # يتم تخزين مفتاح التشفير الفعلي (K_mod_26) داخل دالة encrypt_char()
        CipTxt += encrypt_char(n, cipher_key_large)

    # ... حسابات الطول (إزالة الطباعة من الدالة لتبسيطها) ...

    return CipTxt

# --- فك التشفير (Decryption) ---

# 1. الدالة المساعدة: حساب معكوس الضرب الموديلو
def mod_inverse(a, m):
    """تحسب المعكوس الموديلو لـ a بالنسبة لـ m."""
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None # إذا لم يتم العثور على معكوس (وهذا لا ينبغي أن يحدث في حالتنا)

# 2. دالة فك التشفير الرئيسية
def decrypt_char(char, key):
    """فك تشفير حرف واحد باستخدام المعكوس الموديلو للمفتاح."""
    if char.isupper():
        base = ord('A')
    elif char.islower():
        base = ord('a')
    else:
        return char

    char_index = ord(char) - base # مؤشر الحرف المشفر (0-25)

    # **المفتاح K هنا هو المفتاح الفعلي (K_mod_26) المخزن في Sec_Key**
    inverse_key = mod_inverse(key, 26)

    if inverse_key is None:
        # هذا لن يحدث إذا كان المفتاح صالحاً (GCD=1)
        return '?' 

    # تطبيق فك التشفير: P = (C * K^-1) mod 26
    plain_index = (char_index * inverse_key) % 26
    
    return chr(plain_index + base)

# 3. دالة تطبيق فك التشفير المتناوب
def apply_alternating_decipher(cipherTxt, SecKey):
    """تطبيق فك التشفير المتناوب باستخدام المفاتيح المخزنة."""
    PlaTxt = ""
    
    for i, c in enumerate(cipherTxt):
        if i < len(SecKey):
            key = SecKey[i]
            PlaTxt += decrypt_char(c, key)
        else:
            PlaTxt += c
            
    return PlaTxt

# --- تنفيذ الكود ---
plaTxt = "helloriyadh" # نص تجريبي

# 1. التشفير
final_cipher_text = apply_alternating_cipher(plaTxt)

# 2. الطباعة
print(f"org txt: {plaTxt}")
print(f"used keys: {Sec_Key}") 
print(f"ciphered txt: {final_cipher_text}")
print("-" * 30)

# 3. فك التشفير
decrypted_text = apply_alternating_decipher(final_cipher_text, Sec_Key)
print(f"decrypt txt: {decrypted_text}")