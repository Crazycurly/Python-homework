board = [[3, 4, 0], [4, 3, 0], [3, 3, 1], [4, 4, 1]]
#board = [[3, 4, 0], [4, 3, 0], [3, 3, 1], [4, 4, 0], [4, 5, 0]]

steps = [[5, 4], [5, 5]]


def getBoard():
    b = []
    for i in range(8):
        b.append(['none'] * 8)
    for index in board:
        if index[2]:
            b[index[0]][index[1]] = 'white'
        else:
            b[index[0]][index[1]] = 'black'
    return b


def getScoreOfBoard(board):
    b = 0
    w = 0
    ans = ''
    for x in range(8):
        for y in range(8):
            if board[x][y] == 'black':
                b += 1
            if board[x][y] == 'white':
                w += 1
    if b > w:
        ans = "black"
    elif b == w:
        ans = "tie"
    else:
        ans = "white"
    return ans


def isOnBoard(x, y):
    return x >= 0 and x <= 7 and y >= 0 and y <= 7


def isValidMove(board, tile, xstart, ystart):
    if not isOnBoard(xstart, ystart) or board[xstart][ystart] != 'none':
        return False

    board[xstart][ystart] = tile

    if tile == 'black':
        otherTile = 'white'
    else:
        otherTile = 'black'

    tilesToFlip = []
    for xdirection, ydirection in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
        x, y = xstart, ystart
        x += xdirection
        y += ydirection
        if isOnBoard(x, y) and board[x][y] == otherTile:
            x += xdirection
            y += ydirection
            if not isOnBoard(x, y):
                continue
            while board[x][y] == otherTile:
                x += xdirection
                y += ydirection
                if not isOnBoard(x, y):
                    break
            if not isOnBoard(x, y):
                continue
            if board[x][y] == tile:
                while True:
                    x -= xdirection
                    y -= ydirection
                    if x == xstart and y == ystart:
                        break
                    tilesToFlip.append([x, y])

    board[xstart][ystart] = 'none'
    if len(tilesToFlip) == 0:
        return False
    return tilesToFlip


def getValidMoves(board, tile):
    validMoves = []

    for x in range(8):
        for y in range(8):
            if isValidMove(board, tile, x, y) != False:
                validMoves.append([x, y])
    return validMoves


def makeMove(board, tile, xstart, ystart):
    tilesToFlip = isValidMove(board, tile, xstart, ystart)

    if tilesToFlip == False:
        return False

    board[xstart][ystart] = tile
    for x, y in tilesToFlip:
        board[x][y] = tile
    return True


def boardTolist(board):
    b = []
    for x in range(8):
        for y in range(8):
            if board[x][y] != 'none':
                b.append([x, y, 0 if (board[x][y] == 'black') else 1])
                # print(x,y,board[x][y])
    return b

def moveStep(board,steps):
    tile = 'black'
    for move in steps:
        makeMove(board, tile, move[0], move[1])
        tile = 'black' if (tile == 'white') else 'white'


mainboard = getBoard()

## First
print(getScoreOfBoard(mainboard))
## Second
print(len(getValidMoves(mainboard, 'black')))
## Third
moveStep(mainboard,steps)
print(boardTolist(mainboard))
