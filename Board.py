__author__ = 'kyleweisel'

from BoardBlock import BoardBlock


class Board:

    blocks = []
    moves = []
    player1Name = None
    player2Name = None
    player1Color = "W"
    playerNextMove = None

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

    def initialize(self):
        with open('game.txt') as f:
            gameFile = [line.rstrip('\n') for line in f]

        for i in range(0, len(gameFile)):

            # These are the names of the players
            if i < 2:
                # Ignore for now
                print "ignoring"

            # These are the colors of the players
            if 2 <= i < 5:
                # Ignore these as well
                print "ignoring"

            # These are the moves we care about
            if i >= 11:
                moveBlock = gameFile[i][:1]
                moveCell = gameFile[i][2:3]
                rotatedBlock = gameFile[i][4:5]
                rotationDirection = gameFile[i][5:6]

                player = 0 if (i % 2 == 1) else 1

                self.blocks[int(moveBlock)-1].cells[int(moveCell)-1] = player

                if rotationDirection == "L":
                    self.blocks[int(rotatedBlock)-1].rotateLeft()
                else:
                   self.blocks[int(rotatedBlock)-1].rotateRight()

    def as_2d_array(self):

        product = []

        for i in range(0, 3):
            line = self.blocks[0].getLine(i) + self.blocks[1].getLine(i)
            product.append(line)

        for i in range(0, 3):
            line = self.blocks[2].getLine(i) + self.blocks[3].getLine(i)
            product.append(line)

        return product