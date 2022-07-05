

The command Parser:
Parser example sentences

Go North
Go to the South
Go To the Kitchen
Hide under the Bed
Pick up the green apple
put the pocket change in the vending machine
open the drawer and put the pocket change inside
put the pocket change in the drawer
use the phone
talk to Fred
Attack the Cobra with the sword
Put on the Scuba Suit
Show the Chicken to Larry

Player should be able to type basic commands to interact with environment example:

Pick up the Coins
Buy the dog treats
Take the Key
Open the Drawer

The verbs or actions such as "Pick Up" or "Open" will be pre-defined by the engine.
The nouns or objects are defined at runtime in the games config files

Help:


Heads Up Display/Screen Overlay:

Player:

Player should be able to move from room to room and navigate the map:

Go North
Go Up
Walk North
Move North

Player should have an inventory that can be inspected


Rooms - The main building block of the game

Environment descriptions can change depending on where the player is in the game
How many times the room has been visited
Special events that may change the description of a room
Player state
Can Contain puzzles
Events (Discussed Below)

Items:
Items can be simple or have slots that can contain other items (i.e. containers or other special cases)
Some items can be combined to form new items

Doors and containers can be locked and unlocked with the proper key

NPC's:
NPC's have their own inventory and can give items or items can potentially be stolen or looted under the right conditions


Dialogue:

references : https://github.com/JonathanMurray/dialog-tree-py
Player should be able to talk to NPC's and trigger Dialogue scenes:
"Talk to hotel clerk" 
Triggers Dialogue Sequence:
Dialogue Sequences are special events that use directed graph where a player makes choices
similar to how you would in an rpg

Dialogue choices can trigger results (I.E. Get an item, Game over, Unlock a door, Get into a fight)

Events:

Reference: https://www.geeksforgeeks.org/mimicking-events-python/
https://www.delftstack.com/howto/python/events-in-python/

Timed events or other external triggers can change the game environment 
NPC's, or Time running out/turns running out

Rooms can have events
Items can have events (I.E combining two items together, placing an item in a pedestal, taking an item etc. triggers an event)
Dialogue can Trigger an Event
Player Interactions with the environment can Trigger Events

A Shop or bartering system where the currency can be defined in the config
I.E. pop caps instead of coins 
A shop interface where players buy and potentially sell items


Need to be able to save and load game and resume where you left off
Each class knows how to serialize and deserialize itself to json

A relatively simple to use reusable core engine 
that is config driven json files loaded to create rooms, items, characters, conversations etc

Project should be well documented using Pep8 docstrings


Classes
Game Object
Container
Room
Character
Player
NPC
