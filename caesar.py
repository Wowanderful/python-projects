alph = ['АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']
direction = input('Choose direction: \n(+) - Encryption \n(-) - Decryption:\n ')
lang = int(input('Choose language: \n0 - Russian \n1 - English: \n'))
step = int(direction + input('Choose rotate number (rotate to right): '))
text = input('Type the text:\n')

for i in text:
    if i.isalpha():
        char = alph[lang][(alph[lang].index(i.upper()) + step) % len(alph[lang])]
        print(char if i.isupper() else char.lower(), end='')
    else:
        print(i, end='')

