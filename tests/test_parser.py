import unittest
from texticular.game_object import GameObject


class ParserTest(unittest.TestCase):

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

        self.parser = Parser(self.commands)

        GameObject("Chicken Soup", {"Main":"For the soul"})
        GameObject("Hotel Clerk", {"Main":"Asshole"})
        GameObject("table", {"Main":"It's got four legs!"})
        GameObject("light", {"Main":"It turns on and off"})
        GameObject("kitchen", {"Main":"you cook food here"})

    def test_invalid_direction(self):
        parsed_command = self.parser.tokenize("Go Forth", GameObject.objects_by_key)
        print(vars(parsed_command))
        self.assertEqual(parsed_command.response, "FORTH is not a valid direction.")


if __name__ == '__main__':
    unittest.main()
