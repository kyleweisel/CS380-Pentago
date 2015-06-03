__author__ = 'kyleweisel'


class Move:

    boardNum = None
    cellNum = None
    rotatedBoardNum = None
    rotationDirection = None

    def __init__(self, bN=-1, cN=-1, rBN=-1, rD="R"):
        self.boardNum = bN
        self.cellNum = cN
        self.rotatedBoardNum = rBN
        self.rotationDirection = rD