from enum import Enum, auto

class Direction(Enum):
    NORTH = 1
    UP = 1
    NORTHEAST = 5
    EAST = 3
    RIGHT = 3
    SOUTHEAST = 7
    SOUTH = 2
    DOWN = 2
    SOUTHWEST = 8
    WEST = 4
    LEFT = 4
    NORTHWEST = 6

class GameState(Enum):
    EXPLORATION = 1
    DIALOGUESCENE = 2
    GAMEOVER = 3

class Flag(Enum):
    #the player can pick up and carry the object.
    TAKEBIT = auto()
    CONTAINERBIT = auto()


if __name__ == "__main__":
    for direction in Direction:
        print(direction)

    print(repr(Direction.SOUTH))

    print(Direction.NORTH.value)

    try:
        print(Direction["GORTH"])
    except KeyError:
        print("Not a valid direction")

