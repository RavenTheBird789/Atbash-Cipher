# Numerical Atbash Cipher

import time
import os

def purple(text: str) -> str:
    # Wrap text in ANSI codes for purple color
    return f"\033[35m{text}\033[0m"

def bold(text: str) -> str:
    # Wrap text in ANSI codes for bold formatting
    return f"\033[1m{text}\033[0m"

def num_atbash_cipher():
    os.system('cls' if os.name == 'nt' else 'clear')
    user_input = input(purple("Enter a string of digits to invert (0-9): "))
    ciphered_output = ""
    for int in user_input:
        if int.isdigit():
            ciphered_output += chr(ord('9') - (ord(int) - ord('0'))) # Inverts digits from '0' to '9'
        else:
            ciphered_output += int # Non-digit characters added without changes
    print(purple(bold("Ciphered output:")), purple(bold(ciphered_output)))
    time.sleep(1)
    user_request = input(purple("Would you like to use the Numerical Atbash Cipher again? (yes/no): "))
    if user_request.lower() in ['yes', 'y']:
        os.system('cls' if os.name == 'nt' else 'clear')
        num_atbash_cipher()
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        return