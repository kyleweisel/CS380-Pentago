__author__ = 'kyleweisel'


class BoardBlock:

    cells = []

    def __init__(self):
        self.cells = [-1, -1, -1, -1, -1, -1, -1, -1, -1]

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
                temp = self.cells[i]
                line += "-" if (temp == -1) else str(temp)
                #line += str(self.cells[i])

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