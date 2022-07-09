rooms = {1: 'Master Bedroom', 2: 'Living Room',
         3: 'Study', 4: 'Patio',
         5: 'Kitchen', 6: 'Bedroom',
         7: 'Bathroom'}
             # N S E W
roomAccess = [[0,7,2,0,],
              [0,5,3,1,],
              [0,4,0,2,],
              [3,0,0,5,],
              [2,6,4,7,],
              [5,0,0,0,],
              [1,0,5,0,]]

currentRoomIndex = 1

running = True

def printMap():
    print ("""
 _________
|	  |
| M. Bed  |
|________ |
            

""")

directions = {"NORTH": 0,"SOUTH": 1,"EAST": 2,"WEST": 3}

while running:
    printMap()
    print("You are in the " + rooms[currentRoomIndex])
    prompt = input("Which direction do you want to go?\n>>")

    if prompt == "stop":
        running = False
        break
        
    direction = prompt.upper().strip()

    if direction not in directions:
        print("Invalid direction")
    else:
        roomNumber = roomAccess[currentRoomIndex - 1][directions[direction]]
        if roomNumber == 0:
            print("You hit a wall")
        else:
            currentRoomIndex = roomNumber



    
    
