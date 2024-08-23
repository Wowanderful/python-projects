# PASSWORD GENERATOR 
# Run the program and look at the terminal to start 

import random

digits = '0123456789' 
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''

number = input('How many passwords would you like?')
length = input('How many symbols in one password?')
dig = input('Do you need to include digits? Type "y" if yes: ')
upcase = input('Do you need uppercase letters? Type "y" if yes: ')
lowcase = input('Do you need lowercase letters? Type "y" if yes: ')
symb = input('Do you need special symbols? Type "y" if yes: ' )
exlc = input('Would you like to exclude unclear symbols (il1Lo0O) ? Type "y" if yes: ')

if dig == 'y':
    chars += digits
if upcase == 'y':
    chars += uppercase_letters
if lowcase == 'y':
    chars += lowercase_letters
if symb == 'y':
    chars += punctuation
if exlc == 'y':
    for i in 'il1Lo0O':
        chars.replace(i, "")

def generate_password(length, chars):
    password = ''
    for _ in range(int(length)):
        password += random.choice(chars)
    return password

for _ in range (int(number)):
    print(generate_password(length, chars))



