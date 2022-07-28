from game_enums import GameState
import game_controller as gc
from globals import START_ROOM
from game_ui import *
from game_init import setup
from game_object import GameObject


# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.



def go(controller):
    result = ''
    result += "-" * 100 + "\n\n"
    result += "Texticular: Chapter 1 - You Gotta Go!\n\n"
    result += "-" * 100 + "\n\n"
    result += controller.player.go_to(START_ROOM)
    return result





def main_loop():
    setup()
    print("Objects Created...\n\n")
    print(GameObject.objects_by_key)
    controller = gc.Controller()
    ui = UI(controller)
    ui.dialogue.set(go(controller))
    ui.root.mainloop()



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main_loop()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
