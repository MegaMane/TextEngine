import textwrap
import pygame
import globals
from game_enums import Direction, Flag
from game_object import GameObject
from game_controller import Controller
from lexer import Lexer, ParseTree

# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def game_init():
    controller = Controller(Lexer())
    return controller

def go():
    print("This is the intro")

def main_loop():
    while True:
        command = input(">>")
        if command.lower() in ["stop", "quit", "exit", "end"]:
            exit_game()
            break
        tokens = Controller.lexer.tokenize(command, GameObject.objects_by_key)
        if not tokens.input_parsed:
            print(tokens.response)
            continue
        update(tokens)
        """
         <PERFORM ,PRSA ,PRSO ,PRSI>
         <COND (<did-this-input-cause-time-to-pass?>
         <call-room-function-with-M-END>
         <CLOCKER>)>>>

        """
        render()

def update(tokens: ParseTree):
    Controller.handle_input(tokens)

def render():
    pass

def exit_game():
    print("Thanks for playing")
def update_globals():
    globals.HAS_POOPED = True




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main_loop()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
