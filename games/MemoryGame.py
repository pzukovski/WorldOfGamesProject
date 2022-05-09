import random
import inflect
from threading import Event
from utils.Utils import clear_terminal


def generate_sequence(difficulty):
    
    guess_me = random.sample(range(1, 101), difficulty)
    clear_terminal()
    print("""Welcome to the MemoryGame. Soon you'll be shown a series of numbers for short period.
Your mission is to remember those numbers and enter them correctly when asked.

Good luck!""")
    Event().wait(6)
    clear_terminal()
    print('Ready? ')
    Event().wait(1)
    print('\n\n\n\n\n\n')
    print(guess_me)
    Event().wait(float(0.7))
    clear_terminal()
    return guess_me


def get_list_from_user(difficulty):
    
    user_guess = []
    p = inflect.engine()  # changes '1' to First, '2' to Second etc.

    for i in range(0, difficulty):  # user inputs appended to a list. each input is checked for numbers only
        item = input(f'Please enter the {(p.ordinal(i + 1))} number: ')
        is_numeric = (item.isdecimal())
        if is_numeric:    # If numeric only, string will be converted to integer and compared to top and bottom values
            item = int(item)
            if (int(item) > 0) and (int(item) < 101):
                user_guess.append(item)    # if in range, the value will be appended to var item
            else:
                user_guess.clear()    # if not in rage, the var item will be cleared
        else:
            user_guess.clear()    # if the user input is not numeric only, the var item will be cleared

    clear_terminal()
    return user_guess


def is_list_equal(user_guess, guess_me):
    
    is_equal = (user_guess == guess_me)    # as both lists contains only integers we can compare them easily.
    if is_equal:
        print('Great. You won! \n\n')
        return True
    if not is_equal:
        print("You guessed wrong. \n\n")
        return False


def play_memory(difficulty):
    
    secret_list = generate_sequence(difficulty)
    user_list = get_list_from_user(difficulty)
    so_is_it = is_list_equal(secret_list, user_list)
    return so_is_it
