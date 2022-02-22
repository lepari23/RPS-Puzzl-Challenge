# Import module
from tkinter import *


# HELP_PAGE = PhotoImage(file="./I didn't make a help page")
global _START_PAGE
global _MAIN_PAGE
global _HELP_PAGE
global _GAME_OVER
global _SINGLE
global _EASY
global pscore
global cscore
global scene
global root
global background
# ^ yucky naming and redup. all basically working like I/O switches


def main():

    init_gui()

    print(_START_PAGE)
    global root
    root = Tk()
    root.geometry("830x585")

    START_PAGE = PhotoImage(file="./images/pages/start_page.png")

    global background
    background = Label(root, image=START_PAGE)
    background.place(x=0, y=0)

    root.bind("<Button-1>", leftclick)
    root.resizable(False, False)
    root.mainloop()


def init_gui():

    global _START_PAGE, _MAIN_PAGE, _GAME_OVER, _HELP_PAGE
    global _SINGLE, _EASY
    _START_PAGE = True
    _MAIN_PAGE, _GAME_OVER, _HELP_PAGE = False, False, False
    _SINGLE, _EASY = True, True

    global pscore, cscore
    pscore, cscore = 0, 0
    print("*"*5000)


# The only action listener, using conditionals to direct flow
def leftclick(event):

    print("clicked at {}:{}".format(event.x, event.y))
    execute(event.x, event.y)


# executes if anything, was clicked... zoinks, inefficient tho
def execute(x, y):

    # most of the clicks will be on the main page
    if _MAIN_PAGE:

        if 130 < x < 220 and 420 < y < 520:

            print("rock")

        elif 370 < x < 495 and 420 < y < 530:

            print("paper")

        elif 620 < x < 750 and 420 < y < 530:

            print("scissors")

    elif _START_PAGE:

        if 600 < x < 800 and 75 < y < 100:

            print("singleround")
            _SINGLE = True
            # hide asterics for best of 3

        elif 600 < x < 800 and 110 < y < 140:

            print("best of three")
            _SINGLE = False
            # hide asterics for single

        elif 720 < x < 800 and 175 < y < 205:

            print("easy mode")
            _EASY = True
            # hide asterics for hard

        elif 720 < x < 800 and 210 < y < 240:

            print("hard mode")
            _EASY = False
            # hide asterics for easy

        elif 265 < x < 390 and 495 < y < 550:

            print("play")
            start_game()
            _START_PAGE = False
            _MAIN_PAGE = True
            MAIN_PAGE = PhotoImage(file="./images/pages/main_page.png")


        elif 455 < x < 590 and 495 < y < 550:

            exit()

        elif 675 < x < 800 and 255 < y < 290:

            print("help")
            _HELP_PAGE = True

    elif _GAME_OVER:

        if 30 < x < 150 and 205 < y < 260:

            print("replay (go back to start)")
            GAME_OVER = PhotoImage(file="./images/pages/game_over.png")
            init_gui()

        elif 220 < x < 355 and 210 < y < 270:

            exit()


if __name__ == "__main__":
    main()
