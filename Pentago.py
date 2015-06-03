__author__ = 'Kyle Weisel'

from Board import Board
from Analyzer import Analyzer

PLAYER_1 = 1
PLAYER_2 = 2


class Pentago:

    board = None
    player1Name = None
    player2Name = None
    playerNextMove = None

    # initializes a game with a board
    def __init__(self):
        self.board = Board()

    def setPlayer1Color(self, color):
        if color.lower() == "b":
            self.board.player1Color = "B"
        else:
            self.board.player1Color = "W"

    def setPlayer1Name(self, name):
        self.player1Name = name

    def setPlayer2Name(self, name):
        self.player2Name = name

    def initialize_from_file(self, fileName):
        with open(fileName) as f:
            gameFile = [line.rstrip('\n') for line in f]

        for i in range(0, len(gameFile)):

            # These are the names of the players
            if i == 0:
                self.player1Name = gameFile[i]

            if i == 1:
                self.player2Name = gameFile[i]

            # Set player 1's color.  We know player 2's has to be the opposite.
            if i == 2:
                self.setPlayer1Color(gameFile[i])

            # These are the moves we care about.  We can recreate the state represented in the file from here.
            if i >= 11:
                moveBlock = gameFile[i][:1]
                moveCell = gameFile[i][2:3]
                rotatedBlock = gameFile[i][4:5]
                rotationDirection = gameFile[i][5:6]

                # Player 1 always goes first
                player = 0 if (i % 2 == 1) else 1

                self.board.blocks[int(moveBlock)-1].cells[int(moveCell)-1] = player

                if rotationDirection == "L":
                    self.board.blocks[int(rotatedBlock)-1].rotateLeft()
                else:
                    self.board.blocks[int(rotatedBlock)-1].rotateRight()

    def save_to_file(self, fileName):
        file = open(fileName, 'w')

        # TODO: Check if we need the \n

        # Print player 1 first name
        file.write(self.player1Name + "\n")

        # Print player 2 first name
        file.write(self.player2Name + "\n")

        # Print player 1 color
        file.write(self.player1Color.upper() + "\n")

        # Print player 2 color
        file.write("B" if self.player1Color.upper() == "W" else "W")

        # Print the player to move next
        file.write(str(int(self.playerNextMove) + 1))

        #

    # TODO: This really doesn't do a great job of checking for valid input
    def readMove(self):

        acceptableInput = False

        while not acceptableInput:
            rawMove = raw_input("Requesting move for player")
            rawMoveParts = rawMove.split(" ")

            moveBoard = None
            moveCell = None
            rotateBoard = None
            rotateDirection = None

            if len(rawMoveParts[0]) == 3:
                try:
                    moveBoard = int(rawMoveParts[0][:1]) + 1
                    moveCell = int(rawMoveParts[0][2:3]) + 1
                except:
                    print "An invalid format was used to enter the move"

            if len(rawMoveParts[1]) == 2:
                try:
                    rotateBoard = int(rawMoveParts[1][:1])
                    rotateDirection = str(rawMoveParts[1][1:2])
                except:
                    print "An invalid format was used to enter the move"

            # Make sure the moveBoard is valid
            if (0 < moveBoard < 5) and (0 < moveCell < 10) and (0 < rotateBoard < 5):
                # Make sure the rotateDirection is valid
                if rotateDirection.upper() == "L" or rotateDirection.upper() == "R":
                    acceptableInput = True

            if not acceptableInput:
                print "A valid format was used to enter a move, but the move itself is invalid"

    def play(self):

        analyzer = Analyzer()
        isOver = False

        while not isOver:
            isOver = True



if __name__ == "__main__":
    '''
    board = Board()
    board.initialize()

    analyzer = Analyzer()

    print "Initialized board looks like:"
    print str(board)

    # -1 = nobody, 0 = player 1, 1 = player 2
    print "The winner of this game is: " + str(analyzer.analyze(board))
    '''
    p = Pentago()
    p.initialize_from_file("game.txt")
    p.setPlayer1Color("b")
    print p.board