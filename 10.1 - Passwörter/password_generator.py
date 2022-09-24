import os, sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import characters, random, userinput

MAX_LENGTH = 255

password = []

def main():
    generate_password()
    display_password()

def generate_password():
    print("Passwortgenerator:")
    
    # Minimum number of uppercases
    uppercases_count = get_minimum_count("Großbuchstaben", 1, MAX_LENGTH - len(password) - 3)
    append_to_password(characters.UPPERCASES, uppercases_count)
    
    # Minimum number of lowercases
    lowercases_count = get_minimum_count("Kleinbuchstaben", 1, MAX_LENGTH - len(password) - 2)
    append_to_password(characters.LOWERCASES, lowercases_count)
    
    # Minimum number of digits
    digits_count = get_minimum_count("Ziffern", 1, MAX_LENGTH - len(password) - 1)
    append_to_password(characters.DIGITS, digits_count)
    
    # Minimum number of symbols
    symbols_count = get_minimum_count("Symbolen", 1, MAX_LENGTH - len(password) - 0)
    append_to_password(characters.SYMBOLS, symbols_count)
    
    # Add extra random characters
    if (len(password) < MAX_LENGTH):
        length = get_password_length(len(password), MAX_LENGTH)
        extra_count = length - len(password)
        append_to_password(characters.CHARACTERS, extra_count)
        
    return random.shuffle(password)
    
def get_password_length(min_length, max_length): 
    return userinput.get_int(
        "- Bitte geben Sie die gewünschte Passwortlänge zwischen {} und {} ein: ".format(min_length, max_length),
        min_length,
        max_length,
    )
    
def get_minimum_count(value_name, min_count, max_count):
    return userinput.get_int(
        "- Bitte geben Sie die gewünschte Mindestanzahl an {} zwischen {} und {} ein: ".format(value_name, min_count, max_count),
        1,
        max_count,
    )

def append_to_password(character_list, count):
    for x in range(count):
        password.append(random.choice(character_list))
        
def display_password():
    print("")
    print("Passwort:", "".join(password))

main()
