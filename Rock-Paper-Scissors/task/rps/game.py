import random

options = ('rock', 'scissors', 'paper')


def winner(u_choice, c_choice):
    if c_choice == u_choice:
        print(f'There is a draw ({c_choice})')
    elif c_choice == options[options.index(u_choice) - 1]:
        print(f'Sorry, but computer chose {c_choice}')
    elif c_choice == options[options.index(u_choice) - 2]:
        print(f'Well done. Computer chose {c_choice} and failed')


while True:
    u_inp = input().strip()
    if u_inp == '!exit':
        print('Bye!')
        break
    elif u_inp not in options:
        print('Invalid input')
        continue
    else:
        winner(u_inp, random.choice(options))
