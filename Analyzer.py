__author__ = 'kyleweisel'


class Analyzer:

    def __init__(self):
        print "Initializing the analyzer"

    def analyze(self, board):

        boardAsList = board.as_2d_array()
        winners = []

        breakILoop = False
        breakJLoop = False

        # For each row
        for i in range(0, 6):

            '''
            if breakILoop:
                continue
            '''

            # For each column
            for j in range(0, 6):

                '''
                if breakJLoop:
                    breakJLoop = False
                    break
                '''

                # Get the value of the current square
                currentValue = boardAsList[i][j]

                if currentValue != -1:

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


        winnersSet = list(set(winners))

        # Will return 0 if white wins, 1 if black wins, -1 if nobody has won
        if len(winnersSet) > 0:
            if len(winnersSet) > 1:
                return 2
            else:
                return winnersSet[0]
        else:
            return -1