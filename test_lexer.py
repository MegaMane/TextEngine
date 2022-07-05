import unittest
from lexer import *
from game_object import GameObject


class LexerTest(unittest.TestCase):

    def setUp(self) -> None:
        self.commands = [
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

        self.lexer = Lexer(self.commands)

        GameObject("Chicken Soup", "For the soul")
        GameObject("Hotel Clerk", "Asshole")
        GameObject("table", "It's got four legs!")
        GameObject("light", "It turns on and off")
        GameObject("kitchen", "you cook food here")

    def test_invalid_direction(self):
        parsed_command = self.lexer.tokenize("Go Forth", GameObject.objects_by_key)
        self.assertEqual(parsed_command.response, "FORTH is not a valid direction.")


if __name__ == '__main__':
    unittest.main()
