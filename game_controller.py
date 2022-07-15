from game_object import GameObject
from game_room import Room
from story_item import StoryItem,Container
from command_parser import Parser, ParseTree
from globals import *
from game_enums import *
import pygame
from pygame.locals import *
import textwrap

class Controller:
    def __init__(self):
        self.parser = Parser(KNOWN_VERBS)
        self.response = ''
        self.command_history = []
        self.user_input = None
        self.tokens = None
        self.gamestate = GameState.EXPLORATION
        self.rooms = Room.rooms
        self.game_objects = GameObject.objects_by_key
        self.commands = {}

        self.set_commands()


    def render(self):
        self.response = ''
        self.get_input()

    def update(self):
        self.parse(self.user_input)
        print(self.response)

    def get_input(self):
        self.user_input = input(">>")
        self.command_history.append(self.user_input)
        self.user_input = self.user_input.lower().strip()

    def parse(self, user_input):
        if user_input in ["stop", "quit", "exit", "end"]:
            self.exit_game()
        else:
            self.tokens = self.parser.tokenize(user_input, GameObject.objects_by_key)

            if not self.tokens.input_parsed:
                self.response = (self.tokens.response)
                return
            else:
                self.handle_input(self.tokens)

    def exit_game(self):
        self.response = ("Thanks for playing")
        self.gamestate = GameState.GAMEOVER

    def handle_input(self, tokens: ParseTree) ->bool:
        print("handle input called")
        print(vars(tokens))
        verb = tokens.verb
        direct_object= tokens.direct_object_key
        indirect_object = tokens.indirect_object

        #Try letting the indirect object handle the input first
        if indirect_object:
            action = self.game_objects[indirect_object].commands.get("Action")
            if action:
                print("indirect object handler")
                if action(tokens, self):
                    return True

        #If that doesn't work try giving the direct object a change to handle the input
        if direct_object:
            action = self.game_objects[direct_object].commands.get("Action")
            if action:
                print("direct object handler")
                if action(tokens, self):
                    print("this is true")
                    return True

        # fall through to the most generic verb response
        print("generic verb handler")
        return self.commands[verb](tokens)


    def eat(self, tokens: ParseTree) ->bool:
        verb = tokens.verb
        direct_object= tokens.direct_object_key
        obj_name = self.game_objects[direct_object].name
        indirect_object = tokens.indirect_object
        if Flag.EDIBLEBIT in self.game_objects[direct_object].flags:
            self.response = f"You eat the {obj_name}.It's delicious, but now it's gone..."
        else:
            self.response = f"I don't think the {obj_name} would agree with you."
        return True

    def look(self, tokens: ParseTree):
        player = self.game_objects["player"]
        player_location = self.game_objects[player.location_key]
        self.response = player_location.describe()

    def set_commands(self):
        self.commands["eat"]  = self.eat
        self.commands["look"] = self.look





