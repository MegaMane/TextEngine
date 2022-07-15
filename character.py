from game_object import GameObject
from game_enums import Flag

class Character(GameObject):
    def __init__(self, key_value: str, name: str, descriptions: dict, location_key: str, hp: int = 100, sex: str = "?",
                 flags=[], commands={}):
        self.hp = hp
        self.name = name
        self.sex = sex

        super().__init__(key_value, name, descriptions, location_key=location_key, flags=flags,
                         commands=commands)

class Player(Character):
    def __init__(self, key_value: str, name: str, descriptions: dict, location_key: str,
                 hp: int = 100, sex: str = "Male", flags=[Flag.PLAYERBIT], commands={}):
        self.hpoo = 80
        super().__init__(key_value, name, descriptions, location_key=location_key, hp=hp, sex=sex, flags=flags,
                         commands=commands)



class NPC(Character):
    pass