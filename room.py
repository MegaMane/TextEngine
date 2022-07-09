from game_object import GameObject
from story_item import StoryItem
from lexer import ParseTree
import json


class Room(GameObject):
    def __init__(self, name: str, description: str, key_value: str = None):
        self.times_visited = 0
        self.items = []
        self.npcs = []
        self.exits = {}
        super().__init__(name, description, key_value)


    def look(self, tokens: ParseTree) -> str:
        response = ""
        response += f"You are in the {self.name}: {self.current_description}\n\n"
        response += "---Exits---\n\n"
        response += self.get_exits()
        return response

    def get_exits(self) ->str:
        response = ''
        for exit in self.exits.keys():
            exit_description = self.exits[exit].connections[self.key_value]["Description"]
            response += (f"To the {exit.name} is the {exit_description}")
        response += "\n\n"
        return response

    def get_items(self):
        pass

    def get_npcs(self):
        pass



class Exit(GameObject):
    def __init__(self, name: str, description: str, connections: dict, key_value: str = None):
        self.connections = connections
        super().__init__(name, description, key_value)


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
            room_list.append(Room(room["name"], room["descriptions"][0]["text"], room["keyValue"]))
        return  room_list

