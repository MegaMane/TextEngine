import json

def load_json(json_file_path):
    with open(json_file_path) as json_file:
        config = json.load(json_file)
    return config

CONFIG = load_json("./Data/rooms.json")

HAS_POOPED = False

BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)

SINGLE_WORD_COMMANDS = ["look", "inventory", "help", "save", "quit"]

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