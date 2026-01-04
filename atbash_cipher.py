# Atbash Cipher

import time
import os

def atbash_cipher():
    user_input = input("Enter text to encode/decode using an Atbash Cipher: ")
    result = ""
    for char in user_input:
        if char.isalpha():
            if char.islower():
                result += chr(ord('z') - (ord(char) - ord('a'))) # Checks distance from 'a' and 'z' for lowercase letters
            else:
                result += chr(ord('Z') - (ord(char) - ord('A'))) # Checks distance from 'A' and 'Z' for uppercase letters
        else:
            result += char # Characters from user input added to result string without changes
    print("Result:", result)
atbash_cipher()
time.sleep(1)
user_request = input("Would you like to use the Atbash Cipher again? (yes/no): ")
if user_request.lower() in ['yes', 'y']:
    os.system('cls' if os.name == 'nt' else 'clear')
    atbash_cipher()
else:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Thank you for using my Atbash Cipher!")
    time.sleep(5)
    os.system('cls' if os.name == 'nt' else 'clear')
    os._exit(0)