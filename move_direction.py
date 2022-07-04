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

if __name__ == "__main__":
    for direction in Direction:
        print(direction)

print(repr(Direction.SOUTH))

print(Direction.NORTH.value)

