

import os
import graphics
from view import Menu

def holdem():
    #display game banner
    Menu.start()
    input('\nPress any key to start.')
    os.system('clear')
    Menu.start()
    graphics.progress_tracker()
    input()


if __name__ == "__main__":
    holdem()


