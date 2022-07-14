def drawRoom(label, roomSize, doors, playerPresent=False):
    rows = roomSize[1] + 1 if (roomSize[1] % 2 == 0) else roomSize[1]
    columns = roomSize[0] + 1 if (roomSize[0] % 2 == 0) else roomSize[0]
    #print(rows)
    #print(columns)
    roomMap = ''
    corner = "+"
    playerSymbol = '(P)'
    npc = '(!)'
    lockedDoor = 'D*'
    openDoor = 'D'
    interactiveObject = '?'
    horizontalWall = '-'
    verticalWall = '|'
    emptySpace = ' '

    labelRow = int(roomSize[1]/2)
    #print(labelRow)

    #northWall = corner + emptySpace + (horizontalWall * (roomSize[0] - 2)) + emptySpace + corner + '\n'
    northWall = corner + emptySpace + lockedDoor.center(roomSize[0] - 2, horizontalWall) + emptySpace + corner + '\n'
    southWall = corner + emptySpace + (horizontalWall * (roomSize[0] - 2)) + emptySpace + lockedDoor + '\n'
    
    row = 0
    roomArea = ''
    while row < rows:

        if row == labelRow:
            roomArea += lockedDoor +  label.center((columns - 1), emptySpace) + lockedDoor + '\n'

        elif playerPresent and row == roomSize[1] - 2:
            roomArea += verticalWall +  playerSymbol.center((columns - 1), emptySpace) + verticalWall + '\n'
        else:
            roomArea += verticalWall + (emptySpace * (columns - 1)) + verticalWall + '\n'

        row += 1

    roomMap +=  northWall + roomArea + southWall

    
    legend = """
    Legend
    ----------------
    D* = locked Door
    D = Open Door
    (P) = player
    (!) = npc
    ? = Secrets left to find
    """
    print(legend)
    print(roomMap)




drawRoom('TestRoom', (26, 7), {'NORTH': ('Door', 'Locked'), 'SOUTH': ('Door', 'Open'),'EAST': ('Door', 'Locked'),'WEST': ('Door', 'Open')}, True)

    
