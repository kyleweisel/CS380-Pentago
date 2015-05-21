__author__ = 'Kyle Weisel'

from Board import Board
from Analyzer import Analyzer

board = Board()
board.initialize()

analyzer = Analyzer()

print "Initialized board looks like:"
print str(board)

# -1 = nobody, 0 = player 1, 1 = player 2
print "The winner of this game is: " + str(analyzer.analyze(board))