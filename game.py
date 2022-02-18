import random

WELCOME_TEXT = \
    """
Welcome to ROCK, PAPER, SCISSORS
Game mode: {}
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

SELECT_TEXT = \
    """
Please enter any one of the acceptable characters below to choose your move:
* Rock:     r, R, 0
* Paper:    p, P, 1
* Scissors: s, S, 2
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

WIN_TEXT = \
    """
YOU WIN!!!

GREAT SUCCESS!! :D
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

LOSE_TEXT = \
    """
YOU LOSE!!!

What a shame... :c
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

DRAW_TEXT = \
    """
DRAW!!!

How anti-climactic :/
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

RESULTS_TEXT = \
    """
MOVES:
 * USER:        {}
 * COMPUTER:    {}
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

INVALID_ENTRY = \
    """
Invalid entry!

Please try again...
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

valid_chars = ['0', '1', '2', 'R', 'P', 'S', 'r', 'p', 's']
moves = ['Rock', 'Paper', 'Scissors']


def main():

    # just in case I wanna add multiple rounds or to make the opponent smarter.
    print(WELCOME_TEXT.format("Single Round"))

    comp_move = generate_move()
    user_move = get_input()
    print(RESULTS_TEXT.format(moves[user_move], moves[comp_move]))

    evaluate(user_move, comp_move)


# simple, fair RNG
def generate_move():
    return int(random.choice(valid_chars[0:3]))


# Using CLI for now because GUI work is super yucky and can take longer
def get_input():

    # Just to ensure user input is always as expected
    while True:

        option = input(SELECT_TEXT)

        if option not in valid_chars:

            print(INVALID_ENTRY)

        else:

            if not option.isnumeric():

                i = ((valid_chars.index(option)) % 3)
                option = valid_chars[i]

            break

    return int(option)


# Simply checks players inputs and displays respective result
def evaluate(user, comp):

    if user == comp:
        print(DRAW_TEXT)

    elif user == 0 and comp == 2:
        print(WIN_TEXT)

    elif user == 2 and comp == 0:
        print(LOSE_TEXT)

    elif user > comp:
        print(WIN_TEXT)

    else:
        print(LOSE_TEXT)


if __name__ == "__main__":
    main()
