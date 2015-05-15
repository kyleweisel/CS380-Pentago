__author__ = 'Kyle Weisel'


class Analyzer:

    def __init__(self):
        print "Initializing the analyzer"

    def analyze(self, board):

        boardAsList = board.as2DArray()
        winners = []

        breakILoop = False
        breakJLoop = False

        # For each row
        for i in range(0, 6):

            if breakILoop:
                continue

            # For each column
            for j in range(0, 6):

                if breakJLoop:
                    break

                # Get the value of the current square
                currentValue = boardAsList[i][j]

                # Check to the left - make sure there is room to go 5 places...
                # TODO: Check these numbers
                if not (j - 4) < 0:
                    isWin = True
                    for k in range(0, 5):
                        if boardAsList[i][j-k] != currentValue:
                            isWin = False
                    if isWin:
                        print "Found a win going left"
                        breakJLoop = True
                        winners.append(currentValue)

                # Check to the right - make sure there is room to go 5 places...
                # TODO: Check these numbers
                if not (j + 4) > 5:
                    isWin = True
                    for k in range(0, 5):
                        if boardAsList[i][j+k] != currentValue:
                            isWin = False
                    if isWin:
                        print "Found a win going right"
                        breakJLoop = True
                        winners.append(currentValue)

                # Check to the down - make sure there is room to go 5 places...
                # TODO: Check these numbers
                if not (i + 4) > 5:
                    isWin = True
                    for k in range(0, 5):
                        if boardAsList[i+k][j] != currentValue:
                            isWin = False
                    if isWin:
                        print "Found a win going down"
                        breakILoop = True
                        winners.append(currentValue)

                # Check to the up - make sure there is room to go 5 places...
                # TODO: Check these numbers
                if not (i - 4) < 0:
                    isWin = True
                    for k in range(0, 5):
                        if boardAsList[i-k][j] != currentValue:
                            isWin = False
                    if isWin:
                        print "Found a win going up"
                        breakILoop = True
                        winners.append(currentValue)

        return winners




class BoardBlock:

    cells = []

    def __init__(self):
        self.cells = [1, 1, 1, 4, 5, 6, 7, 8, 9]

    def __str__(self):

        result = ""

        for i in range(0, len(self.cells)):

            cellValue = self.cells[i]

            if cellValue == 0:
                cellValue = "-"

            # Check if this is the first cell in a row
            if (i % 3) == 0:
                result += "|\t"

            result += cellValue

            # Check if this is the last cell in a row
            if ((i + 1) % 3) == 0 and i != len(self.cells):
                result += "\t|\n"
            else:
                result += "\t"

        return result

    def getLine(self, lineNum):

        if lineNum not in [0, 1, 2]:
            return None
        else:
            startIndex = lineNum * 3
            endIndex = startIndex + 3
            return self.cells[startIndex:endIndex]

    def getLineAsString(self, lineNum):

        if lineNum not in [0, 1, 2]:
            return None
        else:
            startIndex = lineNum * 3
            endIndex = startIndex + 3
            line = ""

            for i in range(startIndex, endIndex):
                line += str(self.cells[i])

                if (i + 1) % 3 != 0:
                    line += "\t"

            return line

    def rotateLeft(self):
        oldCells = self.cells[:]
        self.cells = [oldCells[2], oldCells[5], oldCells[8], oldCells[1], oldCells[4], oldCells[7], oldCells[0],
                      oldCells[3], oldCells[6]]

    def rotateRight(self):
        oldCells = self.cells[:]
        self.cells = [oldCells[6], oldCells[3], oldCells[0], oldCells[7], oldCells[4], oldCells[1], oldCells[8],
                      oldCells[5], oldCells[2]]


class Board:

    blocks = []
    moves = []

    def __init__(self):
        self.blocks = [BoardBlock(), BoardBlock(), BoardBlock(), BoardBlock()]

    def __str__(self):
        result = "+---------------+---------------+\n"
        result += "|            PENTAGO            |\n"
        result += "+---------------+---------------+\n"

        # Print the first and second block
        firstLine = "|\t" + self.blocks[0].getLineAsString(0) + "\t|\t" + self.blocks[1].getLineAsString(0) + "\t|"
        secondLine = "|\t" + self.blocks[0].getLineAsString(1) + "\t|\t" + self.blocks[1].getLineAsString(1) + "\t|"
        thirdLine = "|\t" + self.blocks[0].getLineAsString(2) + "\t|\t" + self.blocks[1].getLineAsString(2) + "\t|"

        result += firstLine
        result += "\n"
        result += secondLine
        result += "\n"
        result += thirdLine
        result += "\n"
        result += "+---------------+---------------+\n"

        # Print the third and fourth block
        fourthLine = "|\t" + self.blocks[2].getLineAsString(0) + "\t|\t" + self.blocks[3].getLineAsString(0) + "\t|"
        fifthLine = "|\t" + self.blocks[2].getLineAsString(1) + "\t|\t" + self.blocks[3].getLineAsString(1) + "\t|"
        sixthLine = "|\t" + self.blocks[2].getLineAsString(2) + "\t|\t" + self.blocks[3].getLineAsString(2) + "\t|"

        result += fourthLine
        result += "\n"
        result += fifthLine
        result += "\n"
        result += sixthLine
        result += "\n"
        result += "+---------------+---------------+\n"

        return result

    def initialize(self):
        with open('game.wei') as f:
            gameFile = [line.rstrip('\n') for line in f]

        for i in range(0, len(gameFile)):

            parts = gameFile[i].split(' ')

            print parts

    def as2DArray(self):

        product = []

        for i in range(0, 3):
            line = self.blocks[0].getLine(i) + self.blocks[1].getLine(i)
            product.append(line)

        for i in range(0, 3):
            line = self.blocks[2].getLine(i) + self.blocks[3].getLine(i)
            product.append(line)

        return product


class Move:

    boardNum = None
    cellNum = None
    rotatedBoardNum = None
    rotationDirection = None

    def __init__(self):
        self.boardNum = -1
        self.cellNum = -1
        self.rotatedBoardNum = -1
        self.rotationDirection = -1

board = Board()
print str(board)
'''
board.blocks[1].rotateLeft()
print str(board)

board.blocks[2].rotateRight()
print str(board)

board.blocks[3].rotateRight()
print str(board)

board.initialize()

print str(board.as2DArray()[5])
'''

analyzer = Analyzer()
print analyzer.analyze(board)