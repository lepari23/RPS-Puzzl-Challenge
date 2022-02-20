import tkinter

valid_chars = ['0', '1', '2', 'R', 'P', 'S', 'r', 'p', 's']
moves = ['Rock', 'Paper', 'Scissors']
hard_mode = False
player, comp = 0, 0
moves_log = []
round = 0


def main():

    comp_move = generate_move()
    user_move = get_input()
    moves_log.append(user_move)
    moves_log.append(comp_move)

    evaluate(user_move, comp_move)

    refresh_gui()


def init_gui():
    # begin loop, wait for input
    print()


def generate_move():
    if hard_mode:

        print("hard_mode")

        # simple winning algo:
        # let P be the last move of the player
        # let X' be the successor to X
        # thus P = R', S = P', R = S'
        # Next move of computer = C
        # C = X''
        # This just follows the one-ahead principle

        return 0

    else:

        return int(random.choice(valid_chars[0:3]))


# modify to return True when R/P/S is clicked
def get_input():
    return False


def evaluate(user, comp):

    if user == comp:
        print("DRAW_TEXT")

    elif user == 0 and comp == 2:
        print("WIN_TEXT")

    elif user == 2 and comp == 0:
        print("LOSE_TEXT")

    elif user > comp:
        print("WIN_TEXT")

    else:
        print("LOSE_TEXT")


def check_score():
    # run while both scores are less than 3


# To be called whenever an image or value needs updating
def refresh_gui():
    print("Refresh")


if __name__ == '__main__':
    main()
