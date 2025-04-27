"""RSA Encryption and Decryption

Original file is located at
https://colab.research.google.com/drive/1FWACZJg66tk4WmDRj7Ft6VoAw_iJEwm9?usp=sharing
"""


import random
from sympy import isprime, mod_inverse

# Generate a random prime number with given bit size
def generate_prime(bits=8):
    while True:
        num = random.randint(2**(bits-1), 2**bits - 1)
        if isprime(num):
            return num

# Generate RSA keys
def rsa_key_generation():
    p = generate_prime()
    q = generate_prime()
    n = p * q
    phi_n = (p - 1) * (q - 1)

    # Choose e such that gcd(e, phi_n) = 1
    e = random.randint(2, phi_n - 1)
    while gcd(e, phi_n) != 1:
        e = random.randint(2, phi_n - 1)

    # Calculate d, the modular inverse of e
    d = mod_inverse(e, phi_n)

    return (p, q, n, phi_n, e, d)

# Encrypt the message using public key
def encrypt(message, e, n):
    numerical_message = [ord(char) for char in message]
    cipher_text = [pow(num, e, n) for num in numerical_message]
    return cipher_text

# Decrypt the message using private key
def decrypt(cipher_text, d, n):
    decrypted_numerical_message = [pow(num, d, n) for num in cipher_text]
    decrypted_message = ''.join([chr(num) for num in decrypted_numerical_message])
    return decrypted_message

# Calculate greatest common divisor
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def main():
    message = input("Enter the message you want to encrypt: ")

    p, q, n, phi_n, e, d = rsa_key_generation()

    cipher_text = encrypt(message, e, n)
    decrypted_message = decrypt(cipher_text, d, n)

    print("\n--- RSA Encryption and Decryption ---")
    print(f"Prime numbers: p = {p}, q = {q}")
    print(f"Public Key: (e = {e}, n = {n})")
    print(f"Private Key: (d = {d}, n = {n})")
    print(f"Original Message: {message}")
    print(f"Encrypted Message: {cipher_text}")
    print(f"Decrypted Message: {decrypted_message}")

if __name__ == "__main__":
    main()
