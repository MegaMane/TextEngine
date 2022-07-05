from itertools import count
from lexer import ParseTree
from typing import List, Optional, Dict


class GameObject:
    _objectid = count(0)
    objects_by_key = {}

    def __init__(self, name: str, description: str, key_value: str = None):
        '''Base class representing all Game Objects.'''
        self.id = next(self._objectid)
        self.name = name
        self.description = description
        self.commands = {}
        self.commands["look"] = self.look
        self.commands["examine"] = self.examine

        if key_value:
            self.key_value = key_value
        else:
            self.key_value = self.create_key_value(name)

        self.objects_by_key[self.key_value] = self

    def look(self, tokens: ParseTree):
        print("looking now")

    def examine(self, tokens: ParseTree):
        print("Upon further examination...I see nothing special.")

    def create_key_value(self, input_string: str, casing: str = "camel"):
        '''Format the string so that it returns an id with no spaces, 
           called by default if no key_value is provided in the constructor

        Parameters
        ----------
        input_string : str
            The string to be formatted as a key value
        casing: can be either "camel" (thisIsCamelCase) or "pascal" (ThisIsPascalCase)


        Returns
        ---------- 
        str
        
        '''

        # TODO check dictionary to see if object key already exists and do something about it
        if not input_string:
            raise ValueError("key value can not be en empty string")

        casing = casing.lower()

        words = input_string.split(" ")

        if casing == "camel":
            words = [word.strip().lower() for word in words[0:1]] + [word.strip().title() for word in words[1:]]
        elif casing == "pascal":
            words = [word.strip().title() for word in words]

        else:
            raise ValueError("casing must be either pascal or camel")

        result = ''.join(words)
        return result


if __name__ == '__main__':
    obj = GameObject("Test Obj", "Test Obj")
    ob2 = GameObject("Test Obj2", "Test Obj2")
    #print(obj.create_key_value("test room", "pascal"))
    #print(obj.__dict__)
    print(GameObject.objects_by_key)