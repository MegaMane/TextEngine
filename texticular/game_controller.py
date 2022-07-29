from game_object import GameObject
from game_room import Room
from command_parser import Parser, ParseTree
from globals import *
from game_enums import *


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
        self.player = GameObject.objects_by_key["player"]
        self.commands = {}
        self.set_commands()



    def update(self)->str:
        if self.gamestate == GameState.GAMEOVER:
            return "Thanks for Playing..."
        if self.parse():
            self.handle_input()
            #player.current_room.end()
            self.clocker()
        return self.response

    def parse(self)->bool:
        user_input = self.user_input
        if user_input in ["stop", "quit", "exit", "end"]:
            self.exit_game()
            return False
        else:
            self.tokens = self.parser.tokenize(user_input, GameObject.objects_by_key)
            if not self.tokens.input_parsed:
                self.response = (self.tokens.response)
                return False
        return True

    def exit_game(self):
        self.response = ("Thanks for playing")
        self.gamestate = GameState.GAMEOVER

    def clocker(self):
        pass

    def handle_input(self) ->bool:
        tokens = self.tokens
        print("handle input called")
        print(vars(tokens))
        verb = tokens.verb
        direct_object= tokens.direct_object_key
        indirect_object = tokens.indirect_object

        if isinstance(tokens.direct_object_key, Direction):
            print("is instance of direction")
            return self.commands[verb](tokens)


        #Try letting the indirect object handle the input first
        if indirect_object:
            target_object = self.game_objects[indirect_object]
            action = target_object.commands.get("Action")
            if action:
                print("indirect object handler")
                if action(self, target=target_object):
                    return True

        #If that doesn't work try giving the direct object a change to handle the input
        if direct_object:
            target_object = self.game_objects[direct_object]
            action = target_object.commands.get("Action")
            if action:
                print("direct object handler")
                if action(self, target=target_object):
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
        if tokens.direct_object:
            self.response = GameObject.objects_by_key.get(tokens.direct_object_key).describe()
        else:
            self.response = GameObject.objects_by_key.get(self.player.location_key).describe()


    def walk(self, tokens: ParseTree):
        print("walk called")
        self.response = self.player.do_walk(Direction[tokens.direct_object.upper()])

    def stand(self, tokens: ParseTree):
        if PLAYERSITTING:
            obj = GameObject.objects_by_key.get(self.player.location_key)
            self.response = f"You get up (from the {obj.name})"
            self.response += self.player.go_to(obj.location_key)
        else:
            self.response = f"You're already standing so not much happens but here just for fun...Get up uh, get on up,"\
                            f"stay on the scene uh...like a sex machine! Now get going."



    def set_commands(self):
        self.commands["eat"]  = self.eat
        self.commands["look"] = self.look
        self.commands["go"] = self.walk
        self.commands["move"] = self.walk
        self.commands["walk"] = self.walk
        self.commands["run"] = self.walk
        self.commands["stand"] = self.stand
        self.commands["get up"] = self.stand
        self.commands["get off"] = self.stand

    #These two methods are not currently in use and hanled by the game_ui.py
    #as part of tkinter main loop
    def render(self):
        self.response = ''
        self.get_input()

    def get_input(self):
        self.user_input = input(">>")
        self.command_history.append(self.user_input)
        self.user_input = self.user_input.lower().strip()





