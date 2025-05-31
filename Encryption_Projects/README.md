# 🔐 Encryptor Tool

*Program:* Python Encryption Program  
*Author:* Abinash Prasana  

## 📌 Description

This is a simple terminal-based text encryption and decryption tool written in Python.  
It works by randomly shuffling all printable characters (letters, digits, symbols) to generate a substitution key.  
It then:
- Encrypts any input message using this key
- Decrypts any encoded message using the same key

It's a fun introduction to basic cipher logic and string manipulation.

---

## 🧠 Features

- Randomized character key generation
- One-to-one character substitution
- Bi-directional encryption and decryption
- Uses Python's string and random libraries

---

## 🛠 How It Works

1. The script creates a shuffled list of characters as the encryption key.
2. It takes user input for plain text.
3. Each character is mapped to the shuffled key to create cipher text.
4. The program then allows decryption by reversing the process using the same key.

---

## ▶ Sample Usage

```bash
Enter a message to be encrypt: Hello@123
The Original Message is: Hello@123
The Encrypted Message is: Wmttr>gML

Enter a keys to be decrypt: Wmttr>gML
The Encrypted Message is: Wmttr>gML
The Decrypted Message is: Hello@123
