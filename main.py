# Atbash Cipher UI

import time
import os
from atbash_cipher import atbash_cipher
from num_atbash_cipher import num_atbash_cipher

def purple(text: str) -> str:
    # Wrap text in ANSI codes for purple color
    return f"\033[35m{text}\033[0m"

def bold(text: str) -> str:
    # Wrap text in ANSI codes for bold formatting
    return f"\033[1m{text}\033[0m"

def red(text: str) -> str:
    # Wrap text in ANSI codes for red color
    return f"\033[31m{text}\033[0m"

def trademark(main):
    def wrapper():
        print(purple(bold("\n" + emptySpace + "Atbash Cipher")))
        print(purple(equalSign * 20))
        print(red("By: RavenTheBird789"))
        print(purple(equalSign * 20))
        print(purple("Please select an option:"))
        print(purple("1. Use the Atbash Cipher"))
        print(purple("2. Use the Numerical Atbash Cipher"))
        print(purple("3. Exit"))
        main()
    return wrapper

equalSign = "="
emptySpace = "   "

@trademark
def main():
    while True:
        choice = input(purple("Enter your choice (1-3): "))
        if choice == '1':
            atbash_cipher()
        elif choice == '2':
            num_atbash_cipher()
        elif choice == '3':
            os.system('clear');
            print(purple(bold("Thank you for using my Atbash Cipher! Goodbye!")))
            time.sleep(5)
            os.system('clear');
            os._exit(0);
        else:
            print(red(bold("Invalid choice. Please try again.")))
            time.sleep(3)
            os.system('clear');
main();