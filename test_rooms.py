import unittest
from lexer import *
import room
from game_enums import Direction


class RoomTest(unittest.TestCase):
    def setUp(self) -> None:
        loader = room.RoomLoader("./Data/rooms.json")
        self.rooms = loader.decode_rooms()
        loader = room.ExitLoader("./Data/rooms.json")
        self.exits = loader.decode_exits()

        # loop through all of rooms and check the exits. Link them to the corresponding rooms
        # using the location attribute of each connection object in the connections
        # dictionary for the exit
        for rm in self.rooms:
            for ext in self.exits:
                try:
                    door = ext.connections[rm.key_value]
                    cardinal_direction = door["direction"].upper()
                    rm.exits[Direction[cardinal_direction]] = ext
                except KeyError:
                    pass
        self.room_201 = room.GameObject.objects_by_key["room201"]
        self.room_201_bathroom = room.GameObject.objects_by_key["bathroom-room201"]




    def test_room_201(self):


        #bathroom_door = self.exits[0]

        #self.room_201.exits[Direction.WEST] = bathroom_door
        for rm in self.rooms:
            print(rm.look(ParseTree()))
            print("-------------------------------------------------------------------")
        self.assertEqual(self.room_201.exits[Direction.WEST].connections[self.room_201.key_value]["description"], "Bathroom Door (Room Side)")


if __name__ == '__main__':
    unittest.main()
