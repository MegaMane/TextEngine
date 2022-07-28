from texticular.items.story_item import StoryItem, Container
import game_room as gr
import character
import game_actions as ga
from globals import *
from game_enums import Flag
from game_object import  GameObject


def setup():

    player = character.Player(key_value="player",
                              name="Jon",
                              descriptions={"Main": "An Angry nerd with dillusions of grandeur."},
                              location_key="room201",
                              inventory=None
                              )

    #load up map (just the rooms and exits )
    room_loader = gr.RoomLoader(ROOM_CONFIG)
    room_loader.decode_rooms()

    #load items to the map
    #item_loader = ItemLoader()
    #items = item_loader.decode_Items(ITEM_CONFIG["items"])







    room_202_key = StoryItem(key_value="key-room202", name="Card",
                          descriptions={"Main": "The Key Card to Room 202"}, location_key="nowhere-land",
                          synonyms=["card"],slots_occupied=1, adjectives=["Room", "202", "Key"])

    room_203_key = StoryItem(key_value="key-room203", name="Card",
                          descriptions={"Main": "The Key Card to Room 203"}, location_key="nowhere-land",
                          synonyms=["card"],slots_occupied=1, adjectives=["Room", "203", "Key"])

    room_204_key = StoryItem(key_value="key-room204", name="Card",
                          descriptions={"Main": "The Key Card to Room 204"}, location_key="nowhere-land",
                          synonyms=["card"],slots_occupied=1, adjectives=["Room", "204", "Key"])

    Janitors_key = StoryItem(key_value="key-supplyCloset", name="Key",
                          descriptions={"Main": "The Keys to the Janitor's Supply Closet"}, location_key="room201-couch",
                          synonyms=["keyring"],slots_occupied=1, adjectives=["Janitor's", "Supply"])

    couch_201 = Container( key_value="room201-couch",
                           name="Couch",
                           descriptions= {"Main": "There is an obnoxious orange couch in the corner",
                                          "Sitting": "It kinda smells a little musty."},
                           location_key="room201",
                           synonyms=["Sofa","Chair"],
                           total_container_slots= 3,
                           adjectives=["Obnoxious", "Orange"],
                           flags= [Flag.CONTAINERBIT]
    )

    couch_201.add_item(Janitors_key)

    couch_201.commands["Action"] = ga.action_room201_couch


if __name__ == "__main__":
    setup()

    print("Objects Created...\n\n")
    print(GameObject.objects_by_key)






