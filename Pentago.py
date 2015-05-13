__author__ = 'Kyle Weisel'


class BoardBlock:
    cells = []

    def __init__(self):
        self.cells = [1, 2, 3, 4, 5, 6, 7, 8, 9]

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


board = Board()
print str(board)

board.blocks[1].rotateLeft()
print str(board)

board.blocks[2].rotateRight()
print str(board)

board.blocks[3].rotateRight()
print str(board)

