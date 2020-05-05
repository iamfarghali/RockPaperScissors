def computer_won(u_chosen):
    if u_chosen == 'rock':
        print('Sorry, but computer chose paper')
    elif u_chosen == 'paper':
        print('Sorry, but computer chose scissors')
    elif u_chosen == 'scissors':
        print('Sorry, but computer chose rock')


computer_won(input().strip())
