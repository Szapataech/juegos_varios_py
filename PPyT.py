import random


def choose_options():
    options = ('piedra', 'papel', 'tijera')
    user_option = input("piedra, papel o tijera => ")
    user_option = user_option.lower()

    if not user_option in options:
        print('esa opcion no es valida')
        #continue
        return None, None

    computer_option = random.choice(options)

    print('User option => ', user_option)
    print('Computer option => ', computer_option)
    return user_option, computer_option

def check_rules(user_option, computer_option, user_win, computer_wins):
    if user_option == computer_option:
            print('Empate')
    elif user_option == 'piedra':
        if computer_option =='tijera':
            print('piedra gana a tijera')
            print('User gana')
            user_win +=1
            
        else :
            print('Papel gana a piedra')
            print('Computer gana')
            computer_wins +=1
    elif user_option =='papel':
        if computer_option == 'piedra':
            print('Papel gana a piedra')
            print('User gana')
            user_win += 1
        else:
            print('Tijera gana a papel')
            print('Computer gana')
            computer_wins += 1
    elif user_option =='tijera':
        if computer_option == 'papel':
            print('tijera gana a papel')
            print('User gana')
            user_win += 1
        else:
            print('piedra gana a tijera')
            print('Computer gana')
            computer_wins +=1
    return user_win, computer_wins
def run_game():
    computer_wins = 0
    user_win = 0
    rounds=1
    while True:
            print('*'* 50)
            print("Round", rounds)
            print ('*'*50)

            print('puntos de usuario', user_win)
            print('puntos de computer', computer_wins)
            rounds += 1

            user_option, computer_option = choose_options() 
            user_win, computer_wins = check_rules(user_option,computer_option,user_win, computer_wins )
          
            if computer_wins ==2:
                print('El ganador es la computadora')
                break

            if user_win == 2:
                print('El ganador es el usuario')
                break
        
run_game()
