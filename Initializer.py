__author__ = 'kyleweisel'


class Initializer:

    def __init__(self):
        print "Initializing the initializer"

    def initialize_from_file(self, fileName, board):
        with open(fileName) as f:
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

                board.blocks[int(moveBlock)-1].cells[int(moveCell)-1] = player

                if rotationDirection == "L":
                    board.blocks[int(rotatedBlock)-1].rotateLeft()
                else:
                   board.blocks[int(rotatedBlock)-1].rotateRight()
