import random
from threading import Event
from utils.Utils import clear_terminal


def mini_welcome(difficulty):
    clear_terminal()
    print(f"Welcome to the Guess game.\nIn this game you'll need to guess a number between 1-{difficulty}. ")
    Event().wait(2)


def generate_number(difficulty):
    
    secret_number = random.randint(1, difficulty)
    # print(secret_number)
    return secret_number


def get_guess_from_user(difficulty):
    
    while True:
        try:
            user_guess = int(input(f'\nPlease enter a number between 1 and {difficulty}: '))
        except ValueError:
            print("Input has to be an integer in the specified range. Please try again. ")
        else:
            if (user_guess > difficulty) or (user_guess < 1):
                print(f"We're sorry but {user_guess} is not a valid input. Please try again. ")
            else:
                return int(user_guess)


def compare_results(secret_number, user_guess):
    
    is_equal = (secret_number == user_guess)
    # print(is_equal)
    return is_equal


def play_guess(difficulty):
    
    mini_welcome(difficulty)
    secret_number = generate_number(difficulty)
    current_guess = get_guess_from_user(difficulty)
    is_equal = compare_results(secret_number, current_guess)
    clear_terminal()
    if is_equal:
        print('Nice one! You won. \n\n')
        return True
    else:
        print("You guessed wrong. \n\n")
        return False
