# Import module
from tkinter import *


root = Tk()

# 830x583 fairly arbitrary size but shouldn't matter, this is just for pc
root.geometry("830x585")
START_PAGE = "./images/pages/start_page.png"
MAIN_PAGE = "./images/pages/main_page.png"
GAME_OVER = "./images/pages/game_over.png"
# ^ entirely superfluous naming and redup. yuck


bg = PhotoImage(file=START_PAGE)

label1 = Label(root, image=bg)
label1.place(x=0, y=0)


root.mainloop()
