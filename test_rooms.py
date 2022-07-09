import unittest
from lexer import *
import room
from game_enums import Direction


class RoomTest(unittest.TestCase):
    def setUp(self) -> None:
        loader = room.RoomLoader("./Data/rooms.json")
        self.rooms = loader.decode_rooms()
        self.room_201 = room.GameObject.objects_by_key["room201"]



    def test_room_201(self):
        bathroom_door_connections = {
            "placeholder": {
                "Description": "Bathroom Door (Bathroom Side)",
                "IsLocked": False,
                "KeyId": None
            },
            self.room_201.key_value: {
                "Description": "Bathroom Door in room 201",
                "IsLocked": False,
                "KeyId": None
            },

        }

        bathroom_door = room.Exit("Bathroom Door",
                                  "The Bathroom Door",
                                  bathroom_door_connections
                                  )

        self.room_201.exits[Direction.WEST] = bathroom_door
        print(self.room_201.look(ParseTree()))
        self.assertEqual(self.room_201.exits[Direction.WEST].connections[self.room_201.key_value]["Description"], "Bathroom Door in room 201")


if __name__ == '__main__':
    unittest.main()
