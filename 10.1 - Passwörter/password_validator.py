import os, sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import characters, userinput

def main():
    password = get_password()
    print("")
    validate_password(password)

def get_password():
    return userinput.get_string("Bitte geben Sie das Passwort zur Bestätigung ein: ", 8, 255)

def validate_password(password):   
    while True:
        
        # Check if the password countains uppercases.
        if not (contains_characters(password, characters.UPPERCASES)):
            print("Das Passwort ist unsicher, da es keine Großbuchstaben enthält.")
            break;
        
        # Check if the password countains lowercases.
        if not (contains_characters(password, characters.LOWERCASES)):
            print("Das Passwort ist unsicher, da es keine Kleinbuchstaben enthält.")
            break;
        
        # Check if the password countains digits.
        if not (contains_characters(password, characters.DIGITS)):
            print("Das Passwort ist unsicher, da es keine Ziffer enthält.")
            break;
        
        # Check if the password countains symbols.
        if not (contains_characters(password, characters.SYMBOLS)):
            print("Das Passwort ist unsicher, da es kein Symbol enthält.")
            break;
        
        print("Dieses Passwort ist sicher.")
        break;

def contains_characters(string, characters_list):
    return any(char in string for char in characters_list)

main()
