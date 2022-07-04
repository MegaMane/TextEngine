import re





class Lexer:
    def __init__(self, known_verbs: list):
        self.known_commands = known_verbs
        self.prepositions = ["in", "on"]
        # through, inside, up, under, over, beside, below, down ...{the apple}

    def tokenize(self, user_input: str, game_objects: dict):
        tokens = ParseTree()
        tokens.unparsed_input = user_input.lower()
        # To split a string with multiple delimiters in Python, use the re.split() method.
        # The re.split() function splits the string by each occurrence of the pattern
        delimiters = "[\s,!.]"
        command_parts = re.split(delimiters, tokens.unparsed_input)
        # split on the delimiters and remove any empty entries
        command_parts = [cmd for cmd in command_parts if cmd]

        if len(command_parts) == 0:
            # exit early command is empty
            return tokens

        verb_offset = self.get_verb(command_parts, parse_tree=tokens)

        if verb_offset == -1:
            # exit early command did not start with a known verb
            return tokens

        # The rest of the input after the verb has been extracted
        # Remove articles
        remaining_input = [cmd for cmd in command_parts[verb_offset:] if cmd not in ["a", "an", "the"]]
        # print(remaining_input)

        preposition_count = self.get_game_objects(remaining_input, tokens, game_objects)

        if preposition_count > 1:
            # exit early shouldn't have more than one preposition in a command
            return tokens

        self.is_parsed(parse_tree=tokens)
        return tokens

    def get_verb(self, command_parts, parse_tree):
        # Search for the Verb
        command_name = ""
        offset = -1
        for command in self.known_commands:
            command_name = ""

            for index, part in enumerate(command_parts):
                command_name = " ".join(command_parts[0:index + 1])
                if command_name in self.known_commands:
                    parse_tree.verb = command_name
                    offset = index + 1
                    break
            if parse_tree.verb is not None:
                break
        return offset

    def get_game_objects(self, remaining_input, parse_tree, game_objects):
        direct_objects = []
        secondary_objects = []

        # Find a preposition if it exists
        preps = [word for word in remaining_input if word in self.prepositions]
        preposition_count = len(preps)

        if len(preps) == 1:
            # prepostion found
            preposition_index = remaining_input.index(preps[0])
            secondary_objects = remaining_input[preposition_index + 1:]
            direct_objects = remaining_input[0:preposition_index]
            #print(secondary_objects)
            #print(direct_objects)

        else:
            direct_objects = remaining_input

        parse_tree.direct_object_key, parse_tree.direct_object = self.find_game_object(direct_objects, game_objects)
        parse_tree.indirect_object_key, parse_tree.indirect_object = self.find_game_object(secondary_objects, game_objects)

        return preposition_count

    def find_game_object(self, token_list: list, game_objects: dict):
        for obj in game_objects.keys():
            object_name = ""

            for index, part in enumerate(token_list):
                # multi word objects keep joining the array until we find a match
                object_name = " ".join(token_list[0:index + 1])
                if game_objects[obj].name.lower() == object_name:
                    return (game_objects[obj].key_value, game_objects[obj].name)

        return (None, None)

    """
               foreach (KeyValuePair<string, GameObject> obj in GameObject.Objects)
            {
                offset = 0;
                string objectName = "";

                for (int i = 0; i < remainingInput.Count; i++)
                {
                    objectName = String.Join(" ", remainingInput.ToArray(), 0, i + 1);
                    offset = i + 1;

                    if (objectName == obj.Value.Name.ToLower())
                    {

                        tokens.DirectObject = objectName;
                        tokens.DirectObjectKeyValue = obj.Key;
                        remainingInput.RemoveRange(0, offset);
                        break;
                    }
                }
            }


            //check direction
            if (tokens.DirectObject == null && remainingInput.Count > 0)
            {

                string directionName = "";

                directionName = GameController.FirstCharToUpper(String.Join("", remainingInput.ToArray()));

                try
                {
                    Direction desiredDirecton = (Direction)Enum.Parse(typeof(Direction), directionName);
                    tokens.DirectObject = directionName;
                }
                
                catch (ArgumentException e)
                {
                    ///GameController.InputResponse.AppendFormat("{0} is not a valid direction. Type Help for more.\n", directionName);
                    tokens.DirectObject = null;
                }

                    
            }
    """

    def is_parsed(self, parse_tree):
        if (parse_tree.verb is not None
                and parse_tree.direct_object_key is not None):
            parse_tree.input_parsed = True

        else:
            parse_tree.input_parsed = False


class ParseTree:
    def __init__(self):
        self.input_parsed = False
        self.verb = None
        self.direct_object = None
        self.direct_object_key = None
        self.indirect_object = None
        self.indirect_object_key = None
        self.unparsed_input = None


if __name__ == "__main__":
    from game_object import GameObject

    soup = GameObject("Chicken Soup", "For the soul")
    clerk = GameObject("Hotel Clerk", "Asshole")
    table = GameObject("table", "It's got four legs!")
    light = GameObject("light", "It turns on and off")
    kitchen = GameObject("kitchen", "you cook food here")

    commands = [
        "backpack",
        "change channel",
        "close",
        "drink",
        "drop",
        "examine",
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
        "put",
        "shut",
        "take",
        "talk to",
        "talk with",
        "unlock",
        "use",
        "turn off",
        "turn on",
        "walk"
    ]
    lexer = Lexer(commands)

    #parsed_command = lexer.tokenize("turn on the light in the kitchen!", GameObject.objects_by_key)
    #parsed_command = lexer.tokenize("drink the chicken soup on the table.", GameObject.objects_by_key)
    parsed_command = lexer.tokenize("talk to the hotel clerk", GameObject.objects_by_key)

    print(parsed_command.__dict__)
    #print(table.__dict__)
    #print(soup.__dict__)
    print(vars(clerk))
