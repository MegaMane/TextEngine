from game_enums import GameState
from game_controller import Controller


# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def game_init():
    import game_init
    controller = Controller()
    return controller

def go():
    print("This is the intro")


def main_loop():
    go()
    controller = game_init()
    while True:
        controller.render()
        controller.update()
        if controller.gamestate == GameState.GAMEOVER:
            break


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main_loop()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
