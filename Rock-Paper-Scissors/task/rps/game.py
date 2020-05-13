import random
options = ('rock', 'scissors', 'paper')


def get_current_score(u_name):
    players_scores = {}
    rating_file = open('rating.txt', 'r')
    for line in rating_file:
        p_info = line.split()
        players_scores[p_info[0]] = p_info[1]
    return int(players_scores[username]) if username in players_scores else 0


def winner(uc, cc, ops):
    if ops == options:
        if uc == cc:
            return 'draw'
        return 'c_won' if cc == ops[ops.index(uc) - 1] else 'u_won'
    else:
        u_choice_index = 0
        for i in range(len(ops)):
            if ops[i] == uc:
                u_choice_index = i
                break
        n_options = [o for i, o in enumerate(ops) if i > u_choice_index]
        n_options += [o for i, o in enumerate(ops) if i < u_choice_index]
        strong_half = [o for i, o in enumerate(n_options) if i < (len(n_options) / 2)]
        weak_half = [o for o in n_options if o not in strong_half]
        if uc == cc:
            return 'draw'
        return 'c_won' if cc in strong_half else 'u_won'


def game(u_choice, opts=options):
    global current_score
    c_choice = random.choice(opts)
    status = winner(u_choice, c_choice, opts)
    if status == 'draw':
        current_score += 50
        print(f'There is a draw ({c_choice})')
    elif status == 'c_won':
        print(f'Sorry, but computer chose {c_choice}')
    elif status == 'u_won':
        current_score += 100
        print(f'Well done. Computer chose {c_choice} and failed')


username = input('Enter your name: ')
current_score = get_current_score(username)
print(f'Hello, {username}')

user_options = input().strip().split(',')
print("Okay, let's start")

while True:
    u_inp = input().strip()
    if u_inp == '!exit':
        print('Bye!')
        break
    elif u_inp == '!rating':
        print(f'Your rating: {current_score}')
    elif u_inp not in options and u_inp not in user_options:
        print('Invalid input')
        continue
    else:
        game(u_inp) if len(user_options) == 1 else game(u_inp, user_options)
