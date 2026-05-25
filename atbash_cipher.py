# Atbash Cipher

import time
import os

def purple(text: str) -> str:
    # Wrap text in ANSI codes for purple color
    return f"\033[35m{text}\033[0m"

def bold(text: str) -> str:
    # Wrap text in ANSI codes for bold formatting
    return f"\033[1m{text}\033[0m"

def atbash_cipher():
    os.system('cls' if os.name == 'nt' else 'clear')
    user_input = input(purple("Enter text to encode/decode using an Atbash Cipher: "))
    result = ""
    for char in user_input:
        if char.isalpha():
            if char.islower():
                result += chr(ord('z') - (ord(char) - ord('a'))) # Checks distance from 'a' and 'z' for lowercase letters
            else:
                result += chr(ord('Z') - (ord(char) - ord('A'))) # Checks distance from 'A' and 'Z' for uppercase letters
        else:
            result += char # Characters from user input added to result string without changes
    print(purple(bold("Result:")), purple(bold(result)))
    time.sleep(1)
    user_request = input(purple("Would you like to use the Atbash Cipher again? (yes/no): "))
    if user_request.lower() in ['yes', 'y']:
        os.system('cls' if os.name == 'nt' else 'clear')
        atbash_cipher()
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        return