from game_object import GameObject
from game_enums import Flag, Direction
import textwrap

import json

class Room(GameObject):
    room_count = 0
    rooms = {}

    def __init__(self, key_value: str, name: str, descriptions: dict, flags=[], commands={}):
        self.times_visited = 0
        self.items = []
        self.npcs = []
        self.exits = {}
        super().__init__(key_value, name, descriptions, location_key="rooms", flags=flags,
                         commands=commands)
        Room.rooms[self.key_value] = self
        Room.room_count += 1

    def describe(self)-> str:
        response = ""
        response += f"You are in the {self.name}: {self.current_description}"
        response += self.get_exit_descriptions()
        response += "\n\n---Exits---\n\n"
        response += self.list_exits()
        return response

    def get_exit_descriptions(self) ->str:
        response = ''
        for exit_direction in self.exits.keys():
            exit_description = self.exits[exit_direction].current_description
            response += (f" To the {exit_direction.name} {exit_description}")
        return response


    def list_exits(self) -> str:
        response = ''
        for exit_direction in self.exits.keys():
            exit_description = self.exits[exit_direction].name
            response += (f"To the {exit_direction.name} is the {exit_description}\n")
        response += "\n\n"
        return response

    def get_items(self):
        pass

    def get_npcs(self):
        pass

class Exit(GameObject):
    def __init__(self, key_value: str, name: str, descriptions: dict, location_key, connection,
                 key_object = None, flags=[], commands={}):
        self.connection = connection
        self.key_object = key_object
        super().__init__(key_value, name, descriptions, location_key=location_key, flags=flags,
                         commands=commands)
        if self.key_object and Flag.LOCKEDBIT not in self.flags:
            self.add_flag(Flag.LOCKEDBIT)




class RoomLoader:
    def __init__(self, config):
        self.config = config

    def decode_rooms(self):
        room_list = []
        for room in self.config["rooms"]:
            descriptions = {}
            for description in room["descriptions"]:
                descriptions[description["label"]] = description["text"]
            if not room["flags"]:
                flags = [Flag["CONTAINERBIT"]]
            else:
                flags = [Flag[flag] for flag in room["flags"]]
            new_room = (Room(key_value=room["keyValue"], name=room["name"], descriptions=descriptions, flags=flags))
            self.add_exits(new_room, room["exits"])
            room_list.append(new_room)
        return room_list

    def add_exits(self, new_room, exits):
        for exit_direction in exits.keys():
            descriptions = {}
            for description in exits[exit_direction]["descriptions"]:
                descriptions[description["label"]] = description["text"]
            new_exit = Exit(
                            key_value=exits[exit_direction]["keyValue"],
                            name=exits[exit_direction]["name"],
                            descriptions=descriptions,
                            location_key=exits[exit_direction]["locationKey"],
                            connection=exits[exit_direction]["connection"],
                            key_object=exits[exit_direction]["keyObject"],
                            flags=exits[exit_direction]["flags"]
            )
            new_room.exits[Direction[exit_direction.upper()]] = new_exit


