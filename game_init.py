from game_enums import Flag,Direction
from story_item import StoryItem, Container
import game_room as gr
import character
import game_actions as ga



player = character.Player(key_value="player",
                          name="Jon",
                          descriptions={"Main": "An Angry nerd with dillusions of grandeur."},
                          location_key="room201")

room_201_descriptions = {"Main": ("As you look around the hotel room you see an old TV with rabbit ears that looks like "
                                 "it came straight out of the 1950's. Against the wall there is a beat up night stand "
                                 "with a little drawer built in to it and an old phone on top. Next to it is a lumpy old "
                                 "bed that looks like it's seen better days, with a dark brown stain on the sheets and "
                                 "a funny smell coming from it. There is an obnoxious orange couch in the corner next to "
                                 "a small window smudged with sticky purple hand prints. The stuffing is coming out of "
                                 "the cushions which are also spotted with purple, and the floor is covered with empyt cans "
                                 "of Fast Eddie's Colon Cleanse.")}
room_201 = gr.Room(key_value="room201", name="Room 201", descriptions=room_201_descriptions, flags=[Flag.CONTAINERBIT])

room_201.exits = {
                    Direction.WEST: gr.Exit(key_value="exits-room201-bathroom",
                                          name="Bathroom Door",
                                          descriptions={"Main": "The Bathroom Door"},
                                          location_key="room201",
                                          connection="bathroom-room201",
                                          key_object=None),
                    Direction.EAST: gr.Exit(key_value="exits-room201-hallway",
                                          name="Hallway Door",
                                          descriptions={"Main":"The Hallway Door"},
                                          location_key="room201",
                                          connection="westHallway",
                                          key_object=None)
                  }







couch_201.commands["Action"] = ga.action_room201_couch

room_201_bathroom_descriptions = dict(
    Main=("You crack open the door to the bathroom and it looks like it's seen better days. "
          "From the smell of it, it looks like someone beat you to it and narrowly escaped a "
          "hard fought battle with an eight pound burrito. The sink is old,yellowed and caked "
          "with brown muck in the corners. The mirror is cracked and something is written on it "
          "in red. You can't quite make it out. But you don't care...you've gotta take a shit! "
          "You rush to be the first in line to make a deposit in the porcelain bank. But just "
          "as you are about to drop it like it's hot you notice there is an angry Great Dane "
          "guarding the toilet and he looks hungry! You quickly shut the door and somehow "
          "manage to not lose your shit (literally). Looks like you have to find somewhere else "
          "to go if you value your junk...and your life.")
)

room_201_bathroom = gr.Room(key_value="bathroom-room201",
                            name="Room 201 - Bathroom",
                            descriptions=room_201_bathroom_descriptions,
                            flags=[Flag.CONTAINERBIT])

couch_201 = StoryItem(key_value="room201-couch", name="Couch",
                      descriptions={"Main": "There is an obnoxious orange couch in the corner"}, location_key="room201",
                      synonyms=["Sofa","Chair"],slots_occupied=999, adjectives=["Orange", "Obnoxious"])


