# Import module
from tkinter import *



START_PAGE = "./images/pages/start_page.png"
MAIN_PAGE = "./images/pages/main_page.png"
GAME_OVER = "./images/pages/game_over.png"
HELP_PAGE = "./I didn't make a help page"
global _START_PAGE, _MAIN_PAGE, _HELP_PAGE, _GAME_OVER, _SINGLE, _EASY
global pscore, cscore
global scene
global root

# ^ entirely superfluous naming and redup. yuck

def main():

    root = Tk()
    root.geometry("830x585")

    scene = PhotoImage(file=START_PAGE)
    label1 = Label(root, image=scene)
    label1.place(x=0, y=0)

    start_game()
    root.bind("<Button-1>", leftclick)
    root.resizable(False, False)
    root.mainloop()


def start_game():

    _START_PAGE = True
    _MAIN_PAGE, _GAME_OVER, _HELP_PAGE = False, False, False
    _SINGLE, _EASY = False, False
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

        elif 600 < x < 800 and 110 < y < 140:

            print("best of three")

        elif 720 < x < 800 and 175 < y < 205:

            print("easy mode")

        elif 720 < x < 800 and 210 < y < 240:

            print("hard mode")

        elif 265 < x < 390 and 495 < y < 550:

            print("play")


        elif 455 < x < 590 and 495 < y < 550:

            exit()

        elif 675 < x < 800 and 255 < y < 290:

            print("help")

    elif _GAME_OVER:

        if 30 < x < 150 and 205 < y < 260:

            print("replay (go back to start)")
            init_gui()

        elif 220 < x < 355 and 210 < y < 270:

            exit()





if __name__ == "__main__":
    main()
