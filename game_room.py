from game_object import GameObject
from game_enums import Flag
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
        #output = textwrap.wrap(response,100)
        #response = '\n'.join(output)
        response += "\n\n---Exits---\n\n"
        response += self.get_exits()
        return response


    def get_exits(self) -> str:
        response = ''
        for exit in self.exits.keys():
            exit_description = self.exits[exit].current_description
            response += (f"To the {exit.name} is the {exit_description}\n")
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






#TODO update JSON "loader" classes

class RoomLoader:
    def __init__(self, json_file_path):
        self.json_file_path = json_file_path
        self.config = self.load_json()

    def load_json(self):
        with open(self.json_file_path) as json_file:
            config = json.load(json_file)
        return config

    def decode_rooms(self):
        room_list = []
        for room in self.config["rooms"]:
            descriptions = {}
            for description in room["descriptions"]:
                descriptions[description["label"]] = description["text"]
            room_list.append(Room(room["name"], descriptions, room["keyValue"]))
        return room_list





class ExitLoader:
    def __init__(self, json_file_path):
        self.json_file_path = json_file_path
        self.config = self.load_json()

    def load_json(self):
        with open(self.json_file_path) as json_file:
            config = json.load(json_file)
        return config

    def decode_exits(self):
        exit_list = []
        for exit in self.config["exits"]:
            descriptions = {}
            for description in exit["descriptions"]:
                descriptions[description["label"]] = description["text"]
            connections = {}
            for connection in exit["connections"]:
                connections[connection["location"]] = connection
        exit_list.append(Exit(exit["name"], descriptions, connections, exit["keyValue"]))
        return exit_list
