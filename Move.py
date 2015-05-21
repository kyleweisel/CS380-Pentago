__author__ = 'kyleweisel'


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