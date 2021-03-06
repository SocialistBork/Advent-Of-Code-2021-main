file = open("input.txt", "r")

dataStr = file.readlines()

data = []
for line in dataStr:
    data.append(line.strip())

xBound = len(data[0])
yBound = len(data)

lowPoints = []

def ifLow(i, j):
    currentValue = int(data[i][j])

    if i != 0 and i != yBound - 1: #Check if on top or bootm
        if j != 0 and j != xBound - 1:
            if int(data[i][j-1]) > currentValue and int(data[i][j+1]) > currentValue and int(data[i+1][j]) > currentValue and int(data[i-1][j]) > currentValue:
                return True
        elif j == 0: #If on left
            if int(data[i][j+1]) > currentValue and int(data[i+1][j]) > currentValue and int(data[i-1][j]) > currentValue:
                return True
        elif j == xBound - 1: #If on right
            if int(data[i][j-1]) > currentValue and int(data[i+1][j]) > currentValue and int(data[i-1][j]) > currentValue:
                return True
    elif i == 0: #If on top
        if j != 0 and j != xBound - 1:
            if int(data[i][j-1]) > currentValue and int(data[i][j+1]) > currentValue and int(data[i+1][j]) > currentValue:
                return True
        elif j == 0:
            if int(data[i][j+1]) > currentValue and int(data[i+1][j]) > currentValue:
                return True
        elif j == xBound - 1:
            if int(data[i][j-1]) > currentValue  and int(data[i+1][j]) > currentValue:
                return True
    elif i == 99: #If on bottom
        if j != 0 and j != len(data[i])-2:
            if int(data[i][j-1]) > currentValue and int(data[i][j+1]) > currentValue and int(data[i-1][j]) > currentValue:
                return True
        elif j == 0:
            if int(data[i][j+1]) > currentValue and int(data[i-1][j]) > currentValue:
                return True
        elif j == len(data[i]) - 2:
            if int(data[i][j-1]) > currentValue and int(data[i-1][j]) > currentValue:
                return True
    return False

for i in range(yBound):
    str = data[i]
    for j in range(len(str)):
        if ifLow(i,j):
            lowPoints.append(int(data[i][j]))

print(sum(lowPoints)+len(lowPoints))
