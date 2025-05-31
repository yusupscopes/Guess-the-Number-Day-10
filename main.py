import random

def start_game():
    print('Hi there! Welcome to the Guess the Number Game!')
    print('I hope you are ready for a challenge!')
    print('I have a number in my mind, and you have to guess it.')

    while True:
        try:
            min_range = int(input('Enter a minimal number here: '))
            max_range = int(input('Enter a maximum number here: '))
            
            if min_range >= max_range:
                print('Your minimum number should be less than your maximum number.')
                continue
            break
        except ValueError:
            print('You need to put in a valid number only')
    
    target_number = random.randint(min_range, max_range)
    attempts = 0
    print(f'Yes, I have chosen a random number between {min_range} and {max_range}.')

    while True:
        try:
            guess = int(input('Take a guess: '))
            attempts += 1
            
            if guess < target_number:
                print('This is actually lower than what I guessed')            
            elif guess > target_number:
                print('This is actually higher than what I guessed')
            else:
                print(f'Yes, your guess is the correct one! The number I picked out was {target_number}. You guessed it in {attempts} attempts.')
                break
        except ValueError:
            print('You need to put in a valid number only')
            continue

    while True:
        play_again = input('Do you want to play again? (yes/no): ').strip().lower()
        if play_again in ['yes', 'y']:
            start_game()
            break
        elif play_again in ['no', 'n']:
            print('Thanks for playing!')
            break
        else:
            print('Invalid choice. Please try again.')
            
start_game()