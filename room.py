from game_object import GameObject



class Room(GameObject):
    def __init__(self, name: str, description: str, key_value: str = None):
        self.times_visited = 0
        super().__init__(name, description, key_value)



