import unittest
import prop
from lexer import ParseTree
from game_enums import Direction


class PropTest(unittest.TestCase):

    def test_Television(self):
        tokens = ParseTree()
        tv = prop.Television(name="Old TV",
                        descriptions={"Main": "an old TV with rabbit ears that looks like it came straight out of the 1950's"},
                        location_key="room201",
                        key_value="oldtv-room201",
                        channel_list = [
                                "Whenever I feel like a sweaty slob, there is one assurance that gives me peace of mind. Deodorant. Just one wipe under each arm pit and I am good to go for days. Heck, I don't even need to shower for one whole week.That's how good this shit is.",
                                "Ever sit on a toilet and have the never ending wipe?  Well, those days are over. I've invented one wipes.  A new form of toilet paper that contains a solution where with just one wipe, you are fresh and clean. Done deal.",
                                "Well, I'm your Vita-vega-vittival girl. Are you tired? Run-down? Listless? Do you poop out at parties? Are you unpoopular? Well, are you? The answer to all your problems is in this little ol' bottle…Vitameatavegemin. That's it. Vitameatavegemin contains vitamins, meat, meg-e-tables, and vinerals. So why don't you join the thousands of happy , peppy people and get a great big bottle of Vita-veaty-vega-meany-minie-moe-amin. I'll tell you what you have to do. You have to take a whole tablesppon after every meal. It's so tasty, too: it's just like candy. So everybody get a bottle of…this stuff.",
                                "Static..."
                        ],
                        turn_on_response = "You turn on the TV...",
                        turn_off_response = "The TV flickers then goes black."
                        )
        print(tv.turn_on(tokens))
        print(tv.change_channel(tokens))
        print(tv.change_channel(tokens))
        print(tv.change_channel(tokens))
        print(tv.change_channel(tokens))
        print(tv.turn_off(tokens))
        self.assertEqual(tv.name,"Old TV")


if __name__ == '__main__':
    unittest.main()
