from game_object import GameObject
from lexer import ParseTree


class StoryItem(GameObject):
    def __init__(self, name: str, descriptions:dict, location_key=None, is_portable=False, weight=0,
                 key_value: str = ""):
        self._location_key = location_key
        self.synonyms = []
        self.adjectives = []
        self.is_portable = is_portable
        self.weight = weight
        self.slots_occupied = 1
        super().__init__(name, descriptions, key_value)

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

class Container(StoryItem):
    def __init__(self, name: str, descriptions: dict, slots: int = 10, items: list = [], location_key: str = None, is_portable: bool = False,
                 weight: int = 999, key_value: str = ""):
        self.items = []
        self.slots_occupied = 0
        self.slots = slots
        super().__init__(name, descriptions, location_key, is_portable, weight, key_value)

    def add_items(self, items):
        for item in items:
            if isinstance(item, StoryItem):
                if item.slots_occupied <= (self.slots - self.slots_occupied):
                    item.location_key = self.key_value
                    self.items.append(item)
                    self.slots_occupied += item.slots_occupied
                else:
                    raise OverflowError(f"Container ony has {self.slots} slots and {self.slots_occupied} are full."
                                        f"{item.name} takes up {item.slots_occupied} slots. That shit won't fit!")
            else:
                raise ValueError ("You can't put a non-story item into a container")


class Currency(StoryItem):
    pass






if __name__ == "__main__":
    from lexer import ParseTree
    trinket = StoryItem("Trinket", {"Main": "A fun little bauble, but not really useful"}, "Kitchen")
    table = GameObject("table", {"Main":"It's got four legs!"})
    print(trinket.location_key)
    trinket.location_key = "table"
    print(trinket.location_key)
    #print(trinket.active_description)
    print(trinket.commands["examine"](ParseTree()))
