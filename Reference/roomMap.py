def drawRoom(label, roomSize, doors, playerPresent=False):
    rows = roomSize[1] + 1 if (roomSize[1] % 2 == 0) else roomSize[1]
    columns = roomSize[0] + 1 if (roomSize[0] % 2 == 0) else roomSize[0]
    roomMap = ''
    playerSymbol = '(@)'
    npc = '(!)'
    lockedDoor = 'D*'
    openDoor = 'D'
    interactiveObject = '?'
    horizontalWall = '-'
    verticalWall = '|'
    emptySpace = ' '

    labelRow = int(roomSize[1]/2)
    print(labelRow)

    northWall = emptySpace + (horizontalWall * (roomSize[0] - 2)) + emptySpace + '\n'
    southWall = emptySpace + (horizontalWall * (roomSize[0] - 2)) + emptySpace + '\n'
    
    row = 0
    roomArea = ''
    while row < rows:

        if row == labelRow:
            print('label')
            roomArea += verticalWall +  label.center((columns - 2), emptySpace) + verticalWall + '\n'

        elif playerPresent and row == roomSize[1] - 2:
            roomArea += verticalWall +  playerSymbol.center((columns - 2), emptySpace) + verticalWall + '\n'
        else:
            roomArea += verticalWall + (emptySpace * (columns - 2)) + verticalWall + '\n'

        row += 1

    roomMap += northWall + roomArea + southWall

    

    print(roomMap)


drawRoom('TestRoom', (26, 7), {'NORTH': ('Door', 'Locked'), 'SOUTH': ('Door', 'Open'),'EAST': ('Door', 'Locked'),'WEST': ('Door', 'Open')}, True)

    
