from itertools import count
from texticular.command_parser import ParseTree
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
        self.commands["look"] = self.describe
        self.commands["examine"] = self.examine

        if GameObject.objects_by_key.get(key_value):
            # The keyvalue is not unique it already exists in the global game dict
            # print(GameObject.objects_by_key.get(result).name, GameObject.objects_by_key.get(result))
            # print(self.name, self)
            # print(GameObject.objects_by_key)
            raise ValueError(f"Each game object must have a unique key value. {key_value} already exists on "
                             f"Object: {GameObject.objects_by_key.get(key_value).name}:"
                             f" {GameObject.objects_by_key.get(key_value)}")
        else:
            self.key_value = key_value
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


    def describe(self)-> str:
        response = ""
        response += f"{self.name}: {self.current_description} "
        return response

    def examine(self, tokens: ParseTree) ->str:
        print("Upon further examination...I see nothing special.")



