from itertools import count
from command_parser import ParseTree
import re
from typing import List, Optional, Dict


class GameObject:
    """A Base Class representing a generic game object

    Provides some basic functionality for commands that can be used on all objects (i.e. Look and Examine).
    As well as a class level dictionary that keeps track of all game objects that are instantiated.

    Attributes
    ----------
    objects_by_key: dict
        A class level dictionary that keeps track of all the game objects created
        key_value >> GameObject
    id: int
        A globally unique integer ID assigned to each item that is created
    name: str
        The friendly name of the game object
    description: str
        The description of the game object
    commands: dict
        A dictionary of available commands or actions that can be performed with the game object
    key_value: str
        A string identifier for the object containing no spaces that should be unique if possible,
        but is guaranteedto be unique because it is combined with the id attribute.


    Methods
    -------

    create_key_value(input_string, casing= "camel")
        creates a unique key value by combining the key value that is passed in
        (or generated if none is passed) with the id attribute
    """

    _objectid = count(1)
    objects_by_key = {}

    @classmethod
    def get_component(key_value:str):
        pass

    def __init__(self, key_value: str, name: str, descriptions: dict, location_key=None, flags=[], commands={}):
        """
        Parameters
        ----------
       key_value: str
            A string identifier for the object containing no spaces that should be globally unique,
            dashes can be used in place of spaces if multiple words are necessary.

        name : str
            The friendly name of the game object

        current_description: str
            The current description of the game object

        descriptions: dict
            Dictionary containing all possible descriptions of a game object
            First Description = The verbose description the first time you encounter an object before you pick it up
            Short Description = Name
            Location Description = The description of an object if it is on the ground in the room

        location_key: string
            The current location of the game object (another game object such as a room or container)
            or None if the object has been consumed and is out of play

        flags: list
            A list of the type game_enums.Flag that specifies attributes of the item

        commands: dict
            A dictionary of available methods of the object that can be called
        """
        self.id = next(GameObject._objectid)
        self.name = name
        self.descriptions = descriptions
        self.current_description = self.descriptions.get("Main", self.name)
        self._location_key = location_key
        self.flags = flags
        self.commands = commands
        self.commands["look"] = self.look
        self.commands["examine"] = self.examine
        self.key_value = self.create_key_value(key_value)


        GameObject.objects_by_key[self.key_value] = self

    @property
    def location_key(self):
        return self._location_key

    @location_key.setter
    def location_key(self, value):
        location = GameObject.objects_by_key.get(value)
        if location is not None:
            self._location_key = value
        else:
            raise ValueError(f"Location Key {value} does not exist. Please check again.")

    def move(self, other_object_key_value):
        """Puts object1 into object2.
        Example:
            bread.move("toaster")
        """
        self.location_key = other_object_key_value

    def remove(self):
        """Remove the object from the game setting its location to None

        Example:
            key.remove()
        """
        self._location_key = None

    def add_flag(self, flag):
        self.flags.append(flag)

    def remove_flag(self,flag_to_remove):
        # make sure to remove all instances of the flag in case duplicates have been added
        # when calling the add_flag method
        self.flags = [flag for flag in self.flags if flag != flag_to_remove]


    def look(self, tokens: ParseTree) ->str:
        print("looking now")

    def examine(self, tokens: ParseTree) ->str:
        print("Upon further examination...I see nothing special.")

    def create_key_value(self, input_string: str, casing: str = "camel") -> str:
        """Generate a Key value for the game object being created.

        Format the string so that it returns a key value with no spaces,
        in camel case

        Parameters
        ----------
        input_string : str
            The string to be formatted as a key value
        casing: str, optional
            can be either "camel" (thisIsCamelCase) or "pascal" (ThisIsPascalCase)
            (default is camel)

        Raises
        ------
        ValueError
            If the key value passed in is an empty string

        ValueError
            If the key value passed already exists in the game object dictionary

        Returns
        ---------- 
        str
            The generated key value for the game object
        """

        if not input_string:
            raise ValueError("key value can not be en empty string")

        casing = casing.lower()
        delimiters = "[\s,!.]"
        words = re.split(delimiters, input_string)
        #words = input_string.split(" ")

        if casing == "camel":
            words = [word.strip().lower() for word in words[0:1]] + [word.strip().title() for word in words[1:]]
        elif casing == "pascal":
            words = [word.strip().title() for word in words]

        else:
            raise ValueError("casing must be either pascal or camel")

        result = ''.join(words)

        if GameObject.objects_by_key.get(result):
            #The keyvalue is not unique it already exists in the global game dict
            raise ValueError(f"Each game object must have a unique key value. {input_string} already exists as "
                             f"KeyVaue: {result} on another object")
        return result


