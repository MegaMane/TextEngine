from story_item import StoryItem
from game_object import GameObject
from lexer import ParseTree


class Prop(StoryItem):
    def __init__(self,name: str, descriptions: dict, location_key=None, is_portable=False, weight=999,
                 key_value: str = "", container = None):
        self.container = container
        super().__init__(name, descriptions, location_key, is_portable, weight, key_value)


class Television(Prop):
    def __init__(self, name: str, descriptions: dict, location_key=None, key_value: str = "", channel_list:list = [],
                     turn_on_response = "You turn on the TV...", turn_off_response= "The TV flickers then goes black."):
        self.channels = channel_list
        self.current_channel = 0
        self.turn_on_response = turn_on_response
        self.turn_off_response = turn_off_response
        self.is_on = False

        if len(self.channels) == 0:
            self.channels.append("Static...")

        super().__init__(name, descriptions, location_key, is_portable=False, weight=999, key_value=key_value)

        self.commands["change channel"] = self.change_channel
        self.commands["turn on"] = self.turn_on
        self.commands["power on"] = self.turn_on
        self.commands["turn off"] = self.turn_off
        self.commands["power off"] = self.turn_off


    def change_channel(self, tokens: ParseTree) ->str:
        response = ""
        if self.is_on:
            if self.current_channel < len(self.channels) - 1:
                self.current_channel += 1
                response += "\n\nClick..." + self.channels[self.current_channel]
                return response
            else:
                self.current_channel = 0
                response += "\n\nClick..." + self.channels[self.current_channel]
                return response
        else:
            return "You have to turn the TV on first!\n"

    def turn_on(self, tokens: ParseTree) ->str:
        self.is_on = True
        response = ""
        response += "Click..." + self.turn_on_response + "\n\n" + "-------------------------\n\n" + self.channels[self.current_channel]
        return response

    def turn_off(self, tokens: ParseTree) ->str:
        self.is_on = False
        return "\n\n" + self.turn_off_response


class Phone(Prop):
    pass
