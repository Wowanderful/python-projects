import random
new_game = 'y'
answers = ["Absolutely",
            "Certainly", 
            "No doubt", 
            "Definitely yes", 
            "You can be sure", 
            "It seems to me - yes", 
            "Highly likely", 
            "Good perspective", 
            "The signs say yes", 
            "Yep", 
            "Not clear, try again", 
            "Ask later", 
            "Better not to tell", 
            "Can't say at this moment", 
            "Get it together and ask again", 
            "Don't even think of it", 
            "My answer is no", 
            "According to my data - no", 
            "No perspectives", 
            "Highly doubtfully"]

print('Hello world, I am a magic ball, and I know the answer to any question.')
name = input('What is your name, my firend?')
print('Hey,', name)

while new_game == 'y':
    q = input('Please ask your question:')
    print(random.choice(answers))
    again = input('Want to ask anything more? If yes, press "y", if no press "n"')
    if again != 'y':
        print('Come back if you want to ask anything. Farewell!')
        break