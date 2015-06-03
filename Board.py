__author__ = 'kyleweisel'

from BoardBlock import BoardBlock
from Move import Move


class Board:

    blocks = []
    moves = []
    player1Color = "W"

    def __init__(self):
        self.blocks = [BoardBlock(), BoardBlock(), BoardBlock(), BoardBlock()]

    def __str__(self):
        result = "+---------------+---------------+\n"
        result += "|            PENTAGO            |\n"
        result += "+---------------+---------------+\n"

        # Print the first and second block
        firstLine = "|\t" + self.blocks[0].getLineAsPrettyString(0) + "\t|\t" + self.blocks[1].getLineAsPrettyString(0) + "\t|"
        secondLine = "|\t" + self.blocks[0].getLineAsPrettyString(1) + "\t|\t" + self.blocks[1].getLineAsPrettyString(1) + "\t|"
        thirdLine = "|\t" + self.blocks[0].getLineAsPrettyString(2) + "\t|\t" + self.blocks[1].getLineAsPrettyString(2) + "\t|"

        result += firstLine
        result += "\n"
        result += secondLine
        result += "\n"
        result += thirdLine
        result += "\n"
        result += "+---------------+---------------+\n"

        # Print the third and fourth block
        fourthLine = "|\t" + self.blocks[2].getLineAsPrettyString(0) + "\t|\t" + self.blocks[3].getLineAsPrettyString(0) + "\t|"
        fifthLine = "|\t" + self.blocks[2].getLineAsPrettyString(1) + "\t|\t" + self.blocks[3].getLineAsPrettyString(1) + "\t|"
        sixthLine = "|\t" + self.blocks[2].getLineAsPrettyString(2) + "\t|\t" + self.blocks[3].getLineAsPrettyString(2) + "\t|"

        result += fourthLine
        result += "\n"
        result += fifthLine
        result += "\n"
        result += sixthLine
        result += "\n"
        result += "+---------------+---------------+\n"

        # Show the colors on the board properly
        if self.player1Color == "W":
            result = result.replace("0", "W")
            result = result.replace("1", "B")
        else:
            result = result.replace("0", "B")
            result = result.replace("1", "W")

        return result

    def toCompactString(self):
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

        # Show the colors on the board properly
        if self.player1Color == "W":
            result = result.replace("0", "W")
            result = result.replace("1", "B")
        else:
            result = result.replace("0", "B")
            result = result.replace("1", "W")

        return result

    def as_2d_array(self):

        product = []

        for i in range(0, 3):
            line = self.blocks[0].getLine(i) + self.blocks[1].getLine(i)
            product.append(line)

        for i in range(0, 3):
            line = self.blocks[2].getLine(i) + self.blocks[3].getLine(i)
            product.append(line)

        return product

    def rotateBlockLeft(self, blockNumber):
        if 0 <= blockNumber <= 3:
            self.blocks[blockNumber].rotateLeft()

    def rotateBlockRight(self, blockNumber):
        if 0 <= blockNumber <= 3:
            self.blocks[blockNumber].rotateRight()

    def availableMoves(self):

        possibleMoves = []

        for i in range(0, len(self.blocks)):
            for j in range(0, len(self.blocks[i].cells)):
                if self.blocks[i].cellEmpty(j):

                    # Creates moves at i,j with rotations of all blocks left and right
                    for k in range(0, 4):
                        possibleMoves.append(Move(i, j, k, "L"))
                        possibleMoves.append(Move(i, j, k, "R"))

        return possibleMoves