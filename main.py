from game_enums import GameState
from game_controller import Controller
from globals import START_ROOM
from game_ui import *


# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def game_init():
    import game_init
    controller = Controller()
    return controller

def go(controller):
    result = ''
    result += "-" * 100 + "\n\n"
    result += "Texticular: Chapter 1 - You Gotta Go!\n\n"
    result += "-" * 100 + "\n\n"
    result += controller.player.go_to(START_ROOM)
    return result





def main_loop():
    controller = game_init()
    ui = UI(controller)
    ui.dialogue.set(go(controller))
    if controller.gamestate == GameState.GAMEOVER:
        pass
    ui.root.mainloop()



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main_loop()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
