from itertools import count
from lexer import ParseTree
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

    def __init__(self, name: str, description: str, key_value: str = None):
        """
        Parameters
        ----------
        name : str
            The friendly name of the game object
        currentdescription: str
            The current description of the game object
        descriptions: dict
            Dictionary containing all possible descriptions of a game object
        key_value: str, optional
            A string identifier for the object containing no spaces that should be unique if possible,
            but is guaranteedto be unique because it is combined with the id attribute.
        """
        self.id = next(GameObject._objectid)
        self.name = name
        self.descriptions = {}
        self.descriptions["Main"] = description
        self.current_description = self.descriptions["Main"]
        self.commands = {}
        self.commands["look"] = self.look
        self.commands["examine"] = self.examine

        if key_value:
            self.key_value = self.create_key_value(key_value)
        else:
            self.key_value = self.create_key_value(name)

        GameObject.objects_by_key[self.key_value] = self

    def look(self, tokens: ParseTree):
        print("looking now")

    def examine(self, tokens: ParseTree):
        print("Upon further examination...I see nothing special.")

    def create_key_value(self, input_string: str, casing: str = "camel") -> str:
        """Generate a Key value for the game object being created.

        Format the string so that it returns an id with no spaces,
        called by default if no key_value is provided in the constructor

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

        result = ''.join(words) + '-' + str(self.id).zfill(5)
        return result


if __name__ == '__main__':
    obj = GameObject("Test Obj", "Test Obj", "myKey-, val!$")
    ob2 = GameObject("Test Obj2", "Test Obj2")
    #print(obj.create_key_value("test room", "pascal"))
    #print(obj.__dict__)
    print(GameObject.objects_by_key)
    print(ob2.current_description)