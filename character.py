from game_object import GameObject

class Character(GameObject):
    def __init__(self, name, sex, hp = 100, description = '...'):
        self.HP = hp
        self.name = name
        self.sex = sex
        self.description = description

class Player(Character):
    def __init__(self):
        super().__init__(name, sex, hp, description)

class NPC(Character):
    pass