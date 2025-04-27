# 🔐 RSA Encryption and Decryption in Python
# Overview
This project demonstrates a basic RSA encryption and decryption system implemented in Python. It generates public and private keys, encrypts a user-inputted message, and then decrypts it back to its original form.

RSA is a popular asymmetric cryptographic algorithm used for secure data transmission. Unlike symmetric algorithms, RSA uses two different keys: a public key for encryption and a private key for decryption.

# Features
- Random prime number generation

- RSA key generation (public and private keys)

- Message encryption using the public key

- Message decryption using the private key

- Simple user interface for message input

# How It Works

# Encryption Process:
The RSA encryption process involves several steps:
- Key Generation: Two large prime numbers are selected randomly. Their product n becomes part of both the public and private keys.
- A number e is chosen such that it is relatively prime to φ(n) (Euler’s Totient Function of n).
- The public key is the pair (e, n).
- To encrypt a message, each character of the plaintext is converted into its ASCII value and raised to the power of e, modulo n:


# Decryption Process:
- The decryption process in RSA mirrors the encryption process but uses the private key (d, n):
- The private key exponent d is computed such that it is the modular multiplicative inverse of e modulo φ(n).
- The decrypted numerical values are then converted back to characters to recover the original message.

# Requirements
- Python 3.x
- SymPy library
- Install SymPy if you don't have it already:
  (pip install sympy)

# Author
AYON

