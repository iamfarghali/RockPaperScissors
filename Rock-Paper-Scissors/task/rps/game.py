import random

options = ['rock', 'paper', 'scissors']


def winner(u_choice, c_choice):
    if u_choice == 'rock':
        if c_choice == 'paper':
            print(f'Sorry, but computer chose {c_choice}')
        elif c_choice == 'rock':
            print(f'There is a draw ({c_choice})')
        elif c_choice == 'scissors':
            print(f'Well done. Computer chose {c_choice} and failed')
    elif u_choice == 'paper':
        if c_choice == 'paper':
            print(f'There is a draw ({c_choice})')
        elif c_choice == 'rock':
            print(f'Well done. Computer chose {c_choice} and failed')
        elif c_choice == 'scissors':
            print(f'Sorry, but computer chose {c_choice}')
    elif u_choice == 'scissors':
        if c_choice == 'paper':
            print(f'Well done. Computer chose {c_choice} and failed')
        elif c_choice == 'rock':
            print(f'Sorry, but computer chose {c_choice}')
        elif c_choice == 'scissors':
            print(f'There is a draw ({c_choice})')


winner(input().strip(), random.choice(options))


