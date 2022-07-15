HAS_POOPED = False

TILEWIDTH = 16
TILEHEIGHT = 16
NROWS = 36
NCOLS = 28
SCREENWIDTH = NCOLS*TILEWIDTH
SCREENHEIGHT = NROWS*TILEHEIGHT
SCREENSIZE = (SCREENWIDTH, SCREENHEIGHT)

BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

SINGLE_WORD_COMMANDS = ["look", "inventory", "help", "save", "quit"]

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