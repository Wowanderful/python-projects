import random 

new_game = "y"
print("Welcome to Hidden number game!")

def isvalid(n): 
    if n >= 1 and n <= 100:
        return True
    else: 
        return False


while new_game == 'y':
    print('Please type the maximum number that we can use: ')
    upper = int(input())
    number = random.randint(1, upper)
    attempts = 0
    while True:
        print('Print number from 1 to ', upper, ': ')
        n = input()
        nu = int(n)      
        if isvalid(nu): 
            attempts += 1          
            if nu < number: 
                print("Your number is less than the hidden number. Please try again ")
            elif nu > number: 
                print("Your number is more than the hidden number. Please try again ")
            elif nu == number:
                print("You won!")
                print("Number of attempts: ", attempts)
                break
        else: 
            print("May be you will write a natural number from 1 to ", upper, "?")
    print('If you want to play again, type "y"')
    new_game = input()
        

print("Thank you for playing 'Hidden number'. See you soon")
