from currency_converter import CurrencyConverter
from threading import Event
from random import randint
from utils.Utils import clear_terminal


def get_money_interval(difficulty):
    
    c = CurrencyConverter()

    random_sum = float(randint(1, 101))

    rate = c.convert(1, 'USD', 'ILS')
    rate = round(rate, 2)

    value_to_guess = rate * random_sum

    acceptable_guess_range_top = (value_to_guess - (5 - difficulty))
    acceptable_guess_range_top = round(acceptable_guess_range_top, 2)
    acceptable_guess_range_bottom = (value_to_guess + (5 - difficulty))
    acceptable_guess_range_bottom = round(acceptable_guess_range_bottom, 2)

    return [random_sum, acceptable_guess_range_bottom, acceptable_guess_range_top]


def get_guess_from_user(random_sum, acceptable_guess_range_bottom, acceptable_guess_range_top):
    
    clear_terminal()
    print('Welcome to the Currency Roulette Game.\nSoon you will be shown a sum in US Dollars.\n'
          'your task is guessing how much this sum worth in Israeli New Shekel. ')
    Event().wait(5)
    user_guess = input(f'\n\nHow many Israeli Shekels will you get for {random_sum}$? ')
    try:    # trying to catch non number characters
        user_guess = float(user_guess)
    except ValueError:
        print('Oops. Seems like a wrong input. Game Over. ')
        return False
    else:
        if acceptable_guess_range_top >= user_guess >= acceptable_guess_range_bottom:
            print('\nYou are right! ')
            return True
        elif user_guess < acceptable_guess_range_bottom or user_guess > acceptable_guess_range_top:
            print('\nSorry, your answer is too far from the right sum. Game Over. \n\n')
            return False
        else:
            print('\nWrong input. Game Over. \n\n')
            return False


def play_roulette(difficulty):
    
    parameters_list = get_money_interval(difficulty)
    true_of_false = get_guess_from_user(parameters_list[0], parameters_list[2], parameters_list[1])
    if true_of_false:
        return True
    else:
        return False
