from game_object import GameObject



class Room(GameObject):
    def __init__(self, name: str, description: str, key_value: str = None):
        self.times_visited = 0
        self.items = []
        self.exits = {}
        super().__init__(name, description, key_value)


class Exit(GameObject):
    def __init__(self, name: str, description: str, connections: dict, key_value: str = None):

        self.connections = connections
        super().__init__(name, description, key_value)


if __name__ == "__main__":
    from game_enums import Direction
    descript_201 = """As you look around the hotel room you see an old TV with rabbit ears that looks like it came straight
                      out of the 1950's. Against the wall there is a beat up night stand with a little drawer built into it
                      and an old {phone} on top. Next to it is a lumpy old {bed} that looks like it's seen better days with a
                      dark brown stain on the sheets and a funny smell coming from it. There is an obnoxious orange {couch} in
                      the corner next to a small {window} smudged with sticky purple hand prints, the stuffing is coming out of
                      the cushions which are also spotted with purple, and the floor is covered with {cans} of Fast Eddie's Colon
                      Cleanse. """
    room_201 = Room("Room 201", descript_201)

    bathroom_descript = """ You crack open the door to the bathroom and it looks like it's seen better days. From the 
                            smell of it, it looks like someone beat you to it and narrowly escaped a hard fought battle 
                            with an eight pound burrito. The {sink} is old and yellowed. and caked with brown muck in the 
                            corners. The {mirror} is cracked and something is written on it red. You can't quite
                            make it out. But you don't care...you've gotta take a shit! You rush to be the first in line
                            to make a deposit in the porcelain bank {toilet}. But just as you are about to Drop it like 
                            it's hot you notice there is an angry {Great Dane} guarding the toilet and he looks hungry! 
                            You quickly shut the door and somehow manage to not lose your shit (literally). Looks like you 
                            have to find somewhere else to go if you value your junk...and your life.
    """
    room_201_bathroom = Room("Bathroom", descript_201, "Bathroom 201")

    bathroom_door_connections = {
        room_201_bathroom.key_value: {
            "Description": "Bathroom Door (Bathroom Side)",
            "IsLocked": False,
            "KeyId": None
        },
        room_201.key_value: {
            "Description": "Bathroom Door (Room Side)",
            "IsLocked": False,
            "KeyId": None
        },

    }

    bathroom_door = Exit("Bathroom Door",
                         "The Bathroom Door",
                         bathroom_door_connections
                         )

    room_201.exits[Direction.NORTH] = bathroom_door
    room_201_bathroom.exits[Direction.SOUTH] = bathroom_door

    print(room_201_bathroom.exits[Direction.SOUTH].connections[room_201_bathroom.key_value]["Description"])








