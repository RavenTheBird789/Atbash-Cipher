# Numerical Atbash Cipher
import time
import os

def num_atbash_cipher():
    user_input = input("Enter a string of digits to invert (0-9): ")
    ciphered_output = ""
    for int in user_input:
        if int.isdigit():
            ciphered_output += chr(ord('9') - (ord(int) - ord('0'))) # Inverts digits from '0' to '9'
        else:
            ciphered_output += int # Non-digit characters added without changes
    print("Ciphered output:", ciphered_output)
num_atbash_cipher()
time.sleep(1)
user_request = input("Would you like to use the Numerical Atbash Cipher again? (yes/no): ")
if user_request.lower() in ['yes', 'y']:
    os.system('cls' if os.name == 'nt' else 'clear')
    num_atbash_cipher()
else:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Thank you for using my Numerical Atbash Cipher!")
    time.sleep(5)
    os.system('cls' if os.name == 'nt' else 'clear')
    os._exit(0)