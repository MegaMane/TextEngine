from game_object import GameObject
from game_enums import Flag


class StoryItem(GameObject):
    def __init__(self, key_value: str, name: str, descriptions: dict, location_key: str, synonyms: list,
                 slots_occupied: int = 1, adjectives: list = [], flags: list = [], commands: dict = {}):
        self.synonyms = synonyms
        self.adjectives = adjectives
        self.slots_occupied = slots_occupied
        super().__init__(key_value, name, descriptions, location_key=location_key, flags=flags,
                         commands=commands)


    def move(self, other_object: GameObject):
        """Puts object1 into object2.
        Example:
            bread.move("toaster")
        """
        self.location_key = other_object.key_value

    def remove(self):
        """Remove the object from the game setting its location to None

        Example:
            key.remove()
        """
        self._location_key = None

class Currency(StoryItem):
    def __init__(self, key_value: str, name: str, descriptions: dict, location_key: str, value:float,
                 synonyms: list =["Money"], adjectives: list = [], flags: list = [],
                 commands: dict = {}):
        self.value = value
        super().__init__(key_value, name, descriptions, location_key=location_key, synonyms=synonyms, slots_occupied=0,
                         adjectives=adjectives, flags=flags,commands=commands)


class Container(StoryItem):
    def __init__(self, key_value: str, name: str, descriptions: dict, location_key: str, synonyms: list,
                 slots_occupied: int = 99, total_container_slots: int = 10, container_slots_occupied: int = 0,
                 adjectives: list = [], flags: list = [Flag.CONTAINERBIT], commands: dict = {}):
        self.items = []
        self.total_container_slots = total_container_slots
        self.container_slots_occupied = container_slots_occupied

        super().__init__(key_value, name, descriptions, location_key=location_key, synonyms=synonyms,
                         slots_occupied=slots_occupied, adjectives=adjectives, flags=flags, commands=commands)



    def add_item(self, item):
        if isinstance(item, StoryItem):
            if item.slots_occupied <= (self.total_container_slots - self.container_slots_occupied):
                item.move(self)
                self.items.append(item.key_value)
                self.container_slots_occupied += item.slots_occupied
            else:
                raise OverflowError(f"Container ony has {self.total_container_slots} slots and"
                                    f"{self.container_slots_occupied} are full."
                                    f"{item.name} takes up {item.slots_occupied} slots. That shit won't fit!")
        else:
            raise ValueError ("You can't put a non-story item into a container")

    def remove_item(self, item, new_location: str):
        #item_to_remove = [item for item in items if item.name == "yoyo"]
        self.items.remove(item.key_value)
        item.move(new_location)


class Television(StoryItem):
    def __init__(self, key_value: str, name: str, descriptions: dict, location_key: str,
                 synonyms: list = ["Television", "Tube", "Boob Tube"], slots_occupied: int = 99, adjectives: list = [],
                 flags: list = [Flag.SETPIECEBIT], commands: dict = {}, channel_list:list = [],
                 turn_on_response = "You turn on the TV...", turn_off_response= "The TV flickers then goes black."):

        self.channels = channel_list
        self.current_channel = 0
        self.turn_on_response = turn_on_response
        self.turn_off_response = turn_off_response


        if len(self.channels) == 0:
            self.channels.append("Static...")

        super().__init__(key_value, name, descriptions, location_key=location_key, synonyms=synonyms,
                         slots_occupied=slots_occupied, adjectives=adjectives, flags=flags, commands=commands)

        self.commands["change channel"] = self.change_channel
        self.commands["turn on"] = self.turn_on
        self.commands["power on"] = self.turn_on
        self.commands["turn off"] = self.turn_off
        self.commands["power off"] = self.turn_off


    def change_channel(self) ->str:
        response = ""
        if Flag.ONBIT in self.flags:
            if self.current_channel < len(self.channels) - 1:
                self.current_channel += 1
                response += "\n\nClick..." + self.channels[self.current_channel]
                return response
            else:
                self.current_channel = 0
                response += "\n\nClick..." + self.channels[self.current_channel]
                return response
        else:
            return "You have to turn the TV on first!\n"

    def turn_on(self) ->str:
        self.add_flag(Flag.ONBIT)
        response = ""
        response += "Click..." + self.turn_on_response + "\n\n" + "-------------------------\n\n" + self.channels[self.current_channel]
        return response

    def turn_off(self) ->str:
        self.remove_flag(Flag.ONBIT)
        return "\n\n" + self.turn_off_response


class Phone(StoryItem):
    pass





