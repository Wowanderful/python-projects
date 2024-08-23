# THE GAME "HANGMAN"
# Try guessing the word before you get hanged. 
# Run the program and see the terminal

import random

words_list = ["human", "word", "face", "door", "earth", "work", "children", "history", "woman",
            "development", "power", "goverment", "manager", "show", "mobile",
            "economy", "literature", "border", "shop", "president", "employee", "republic", "personality"]

def get_word(list): 
    return random.choice(list)

def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # голова, торс, обе руки, одна нога
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                # голова, торс, обе руки
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                # голова, торс и одна рука
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                # голова и торс
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # голова
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # начальное состояние
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]
    
def print_word(word_, list_):
    for c in word_:
        if c in list_:
            print(c, end=' ')
        else:
            print('_', end=' ')
    print()
    

def play(word):
    # тело функции
    word_completion = '_ ' * len(word)  
    guessed = False                    
    guessed_letters = []               
    guessed_words = []                 
    tries = 6                          
    print('Welcome to the Hangman game!')
    # print(word)
    print(display_hangman(tries))
    print(word_completion)
    while True:
        word_input = input('Please type your letter or word: ')
        # print(word_input)
        if not word_input.isalpha():
            print('This letter is not valid. Please try again: ')
            continue
        if word_input in guessed_words or word_input in guessed_letters:
            print('Sorry, we already have this letter. Please try again: ')
            continue
        if len(word_input) > 1:
            if word_input == word:
                print('Congratulations! You have won the game!')
                break
            else:
                guessed_words.append(word_input)
                tries -= 1
                print(f'Wrong. Tries left: {tries}')
                print(display_hangman(tries))
                print_word(word, guessed_letters)
                if tries == 0:
                    print(f'You are dead. Your word is {word}')
                    break
                continue



        if word_input in word:
            guessed_letters.append(word_input)
            for c in word:
                if c not in guessed_letters:
                    print('This letter is correct!')
                    print_word(word, guessed_letters)
                    guessed = False
                    break
                guessed = True
            if guessed:    
                print_word(word, guessed_letters)
                print('Congratulations! You have won the game!!')
                break
        else:
            guessed_letters.append(word_input)
            tries -= 1
            print(f'Wrong. Tries left: {tries}')
            print(display_hangman(tries))
            print_word(word, guessed_letters)
        if tries == 0:
            print(f'You are dead. Your word is {word}')
            break

while True: 
    play(get_word(words_list))
    if input('Would you like to play again? y / n: ').upper() == 'Y':
        continue
    else:
        break






