import random

options = ('rock', 'scissors', 'paper')
current_score = 0


def winner(u_choice, c_choice):
    global current_score
    if c_choice == u_choice:
        current_score += 50
        print(f'There is a draw ({c_choice})')
    elif c_choice == options[options.index(u_choice) - 1]:
        print(f'Sorry, but computer chose {c_choice}')
    elif c_choice == options[options.index(u_choice) - 2]:
        current_score += 100
        print(f'Well done. Computer chose {c_choice} and failed')


players_scores = {}
username = input('Enter your name: ')
print(f'Hello, {username}')

rating_file = open('rating.txt', 'r')
for line in rating_file:
    p_info = line.split()
    players_scores[p_info[0]] = p_info[1]

current_score = players_scores[username] if username in players_scores else 0

while True:
    u_inp = input().strip()
    if u_inp == '!exit':
        print('Bye!')
        break
    elif u_inp == '!rating':
        print(f'Your rating: {current_score}')
    elif u_inp not in options:
        print('Invalid input')
        continue
    else:
        winner(u_inp, random.choice(options))
