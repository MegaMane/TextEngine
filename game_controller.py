from lexer import Lexer, ParseTree
import globals
from game_object import GameObject

class Controller():
    lexer = Lexer(globals.KNOWN_VERBS)
    response = ''

    @classmethod
    def handle_input(cls, tokens: ParseTree)->str:

        pass