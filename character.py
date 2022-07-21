from game_object import GameObject
from game_enums import Flag, Direction
from game_room import Room
from story_item import  Container


class Character(GameObject):
    def __init__(self, key_value: str, name: str, descriptions: dict, location_key: str, hp: int = 100, sex: str = "?",
                 flags=[], commands={}):
        self.hp = hp
        self.name = name
        self.sex = sex

        super().__init__(key_value, name, descriptions, location_key=location_key, flags=flags,
                         commands=commands)


class Player(Character):
    def __init__(self, key_value: str, name: str, descriptions: dict, location_key: str, inventory: Container,
                 hp: int = 100, sex: str = "Male", flags=[Flag.PLAYERBIT], commands={}):
        self.hpoo = 80
        self.inventory = inventory
        super().__init__(key_value, name, descriptions, location_key=location_key, hp=hp, sex=sex, flags=flags,
                         commands=commands)

    def go_to(self, location_key)-> str:
        """
        It sends the player to that room, and does all the appropriate things such as call
        the room's action routine with M-ENTER, and call the describers. V-WALK, the
        routine which normally handles all movement, calls GOTO; however, there are
        many instances when you will want to call it yourself, such as when the player
        pushes the button in the teleportation booth. Some games allow GOTO to work
        with a vehicle as well as a room.
        Parameters
        ----------
        location_key

        Returns
        -------

        """
        self.location_key = location_key
        #player location changed
        #call rooms action routine
        # call describers
        return GameObject.objects_by_key[location_key].describe()

    def do_walk(self, direction):
        """
        The game will now attempt to walk the player in that direction. Notice the
        difference between GOTO and DO-WALK. DO-WALK is just an attempt, and the
        response might be something like "The door to the west is locked." GOTO
        overides all that, however, and positively sends the player to the given room.

        Parameters
        ----------
        direction

        Returns
        -------

        """
        obj = GameObject.objects_by_key[self.location_key]
        if isinstance(obj,Room):
            room = obj
            exit = room.exits.get(direction)
            if exit:
                if Flag.LOCKEDBIT not in exit.flags:
                    #Everything is good move the player
                    return self.go_to(exit.connection)
                else:
                    key = GameObject.objects_by_key.get(exit.key_object)
                    key_name = (" ".join(key.adjectives) + " " + key.name).strip()
                    for item in self.inventory.items:
                        if item == exit.key_object:
                            exit.remove_flag("LOCKEDBIT")
                            exit.add_flag("OPENBIT")
                            self.inventory.remove(item, exit.key_value)

                            return f"The {exit.name} opens with the {key_name}." + self.go_to(exit.connection)

                    return f"The {exit.name} is locked and you don't have the {key_name}."
            else:
                return "There isn't an exit in that direction!"
        else:
            return f"You can't do that from the {obj.name}!"



class NPC(Character):
    def move(self, location_key):
        """Puts object1 into object2.
        Example:
            janitor.move("mens-bathroom-stall3")
        """
        self.location_key = location_key