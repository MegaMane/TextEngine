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






