import random

user = input('Type in your player name: ')
user_score = 0
computer_score = 0

options = ["rock", "paper", "scissors"]

while True:

    user_choice = input('Select "rock", "paper", "scissors" or [Q]uit: ').lower()

    if user_choice == 'q':
        print(f'See you later, {user} :)')
        break

    if user_choice not in options:
        print('Please, try typing "rock", "paper", "scissors" or [Q]uit')
        continue

    random_choice = random.randint(0, 2)
    # 0 for 'rock', 1 for 'paper', 2 for 'scissors'

    computer_choice = options[random_choice]
    print(f'The computer chose: {computer_choice}\
          You chose: {user_choice}')

    empate1 = random_choice == 0 and user_choice == 'rock'
    empate2 = random_choice == 1 and user_choice == 'paper'
    empate3 = random_choice == 2 and user_choice == 'scissors'

    win1_c = random_choice == 0 and user_choice not in [ "paper", "rock"]
    win2_c = random_choice == 1 and user_choice not in [ "paper", "scissors"]
    win3_c = random_choice == 2 and user_choice not in [ "rock", "scissors"]



    if empate1 or empate2 or empate3:
        print('Its a tie!')
        print(f'{user} socre = {user_score}\
        Computer score = {computer_score}')
        continue
    
    if win1_c or win2_c or win3_c:
        print('One point for the computer!')
        computer_score += 1
        print(f'{user} socre = {user_score}\
        Computer score = {computer_score}')
        continue

    
    else:
        print(f'One point for {user}!')
        user_score += 1
        print(f'{user} socre = {user_score}\
        Computer score = {computer_score}')
        continue
