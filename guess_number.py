import random 

new_game = "д"
print("Добро пожаловать в числовую угадайку")

def isvalid(n): 
    if n >= 1 and n <= 100:
        return True
    else: 
        return False


while new_game == 'д':
    print('Введите максимальное натуральное число которое мы можем загадать: ')
    upper = int(input())
    number = random.randint(1, upper)
    attempts = 0
    while True:
        print('Введите число от 1 до', upper, ': ')
        n = input()
        nu = int(n)      
        if isvalid(nu): 
            attempts += 1          
            if nu < number: 
                print("Ваше число меньше загаданного, попробуйте еще разок")
            elif nu > number: 
                print("Ваше число больше загаданного, попробуйте еще разок")
            elif nu == number:
                print("Вы угадали, поздравляем!")
                print("Количество попыток: ", attempts)
                break
        else: 
            print("А может быть все-таки введем целое число от 1 до", upper, "?")
    print('Если хотите сыграть еще раз напишите "д"')
    new_game = input()
        

print("Спасибо, что играли в числовую угадайку. Еще увидимся...")
