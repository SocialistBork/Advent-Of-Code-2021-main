file = open("file.txt", "r")
data = file.readlines()
numbers = data[0].split(",")

def processBoard(boardIn):
    boardByRow = boardIn.split("\n")
    boardByBoth = []
    for row in boardByRow:
        row.split(" ")
    print(boardByRow)
    return boardByBoth

processBoard(" 3 15  0  2 22\n 9 18 13 17  5\n19  8  7 25 23\n20 11 10 24  4\n14 21 16 12  6")
