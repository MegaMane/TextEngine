from game_object import GameObject


class StoryItem(GameObject):
    def __init__(self, name: str, description: str, location_key=None, is_portable=False, weight=0,
                 key_value: str = ""):
        self._location_key = location_key
        self.is_portable = is_portable
        self.weight = weight
        self.slots_occupied = 1
        super().__init__(name, description, key_value)

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


if __name__ == "__main__":
    from lexer import ParseTree
    trinket = StoryItem("Trinket", {"main": "A fun little bauble, but not really useful"}, "Kitchen")
    table = GameObject("table", "It's got four legs!")
    print(trinket.location_key)
    trinket.location_key = "table"
    print(trinket.location_key)
    print(trinket.active_description)
    print(trinket.commands["examine"](ParseTree()))
