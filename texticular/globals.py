import json
import os

print(os.path.dirname(__file__))
# https://towardsdatascience.com/simple-trick-to-work-with-relative-paths-in-python-c072cdc9acb9

def load_json(json_file_path):
    with open(json_file_path) as json_file:
        config = json.load(json_file)
    return config

ROOM_CONFIG = load_json("../data/rooms.json")
ITEM_CONFIG = load_json("../data/items.json")

HAS_POOPED = False

BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)

SINGLE_VERB_COMMANDS = ["get up", "help", "inventory", "look", "quit", "save"]

START_ROOM = "room201"

KNOWN_VERBS = [
            "backpack",
            "change channel",
            "close",
            "drink",
            "drop",
            "eat",
            "examine",
            "feel",
            "get",
            "get up",
            "get off",
            "go",
            "grab",
            "help",
            "inv",
            "inventory",
            "look",
            "move",
            "open",
            "pick up",
            "power off",
            "power on",
            "pull",
            "put",
            "push",
            "run",
            "shut",
            "sit",
            "stand",
            "take",
            "talk to",
            "talk with",
            "unlock",
            "use",
            "turn",
            "turn off",
            "turn on",
            "walk"
        ]

PLAYERSITTING = False