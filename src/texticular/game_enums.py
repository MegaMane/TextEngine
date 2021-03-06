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
    """
    Enum representing various object attributes that can be added to or removed from an objects "flags" array

    Members
    --------------
    TAKEBIT:
        The player can pick up and carry the object.

    """
    #Special bit to identify the player character
    PLAYERBIT = auto()

    #the player can pick up and carry the object.
    TAKEBIT = auto()

    # The object is a container; thing can be put inside it, it can be opened and closed
    CONTAINERBIT = auto()

    # The object is a surface, such as a table, desk, countertop etc. Any object with SURFACEBIT
    # should have CONTAINERBIT and OPENBIT since you can put thing on the surface but you cant close a counter
    # like you can a box
    SURFACEBIT = auto()

    #The object is part of a room and can only be interacted with in the room but can never be removed
    SETPIECEBIT = auto()

    # Tells routines like open() the object is locked and can't be opened without the proper equipment
    LOCKEDBIT = auto()

    #The item is edible
    EDIBLEBIT = auto()

    #The object is a door and various routines, such as open(), should treat it as such
    DOORBIT = auto()

    #The object is a door or container and is open
    OPENBIT = auto()

    # The object can be worn/is wearable
    WEARBIT = auto()

    # The object is wearable and is currently being worn
    WORNBIT = auto()

    # The object is readable. Any object with a text property should have this bit
    READBIT = auto()

    #The object is capable of providing Light
    LIGHTBIT = auto()

    # The object is on. In the case of a room , this means that the room is lit.
    # Any outdoor room should have an ONBIT. in the case of an object, this means
    # that the object is providing light. On object with the ONBIT should als have the LIGHTBIT
    ONBIT = auto()

    # The object is currency and should be added to the players total funds
    # once taken and not show up as an individual item in inventory
    MONEYBIT = auto


if __name__ == "__main__":
    for direction in Direction:
        print(direction)

    print(repr(Direction.SOUTH))

    print(Direction.NORTH.value)

    try:
        print(Direction["GORTH"])
    except KeyError:
        print("Not a valid direction")

