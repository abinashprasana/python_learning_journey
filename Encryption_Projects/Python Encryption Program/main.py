"""
Encryption & Decryption Program

Author: Abinash Prasana

This is a simple text encryption and decryption tool using character substitution.
It randomly shuffles a list of all printable characters (letters, digits, punctuation, space)
and uses that as a one-time key for encryption and decryption.
"""

import random
import string

# Generate character set and key
chars = " " + string.ascii_letters + string.digits + string.punctuation
chars = list(chars)
key = chars.copy()
random.shuffle(key)

# Encrypt
plain_text = input("Enter a message to encrypt: ")
cipher_text = ""
for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]
print(f"The Original Message is: {plain_text}")
print(f"The Encrypted Message is: {cipher_text}")

# Decrypt
cipher_text = input("Enter the encrypted message to decrypt: ")
plain_text = ""
for letter in cipher_text:
    index = key.index(letter)
    plain_text += chars[index]
print(f"The Encrypted Message is: {cipher_text}")
print(f"The Decrypted Message is: {plain_text}")