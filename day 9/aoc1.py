file = open("input.txt", "r")

data = file.readlines()

lowPoints = []

def ifLow(i, j):
    currentValue = int(data[i][j])
    if i != 0 or i != 99:
        if j != 0 or j != len(data)-1:
            if int(data[i][j-1]) > currentValue and int(data[i][j+1]) > currentValue and int(data[i+1][j]) > currentValue and int(data[i-1][j]) > currentValue:
                return True
        elif j == 0:
            if int(data[i][j+1]) > currentValue and int(data[i+1][j]) > currentValue and int(data[i-1][j]) > currentValue:
                return True
        elif j == len(data) - 1:
            if int(data[i][j-1]) > currentValue and int(data[i+1][j]) > currentValue and int(data[i-1][j]) > currentValue:
                return True
    elif i == 0:
        if j != 0 or j != len(data)-1:
            if int(data[i][j-1]) > currentValue and int(data[i][j+1]) > currentValue and int(data[i+1][j]) > currentValue:
                return True
        elif j == 0:
            if int(data[i][j+1]) > currentValue and int(data[i+1][j]) > currentValue:
                return True
        elif j == len(data) - 1:
            if int(data[i][j-1]) > currentValue  and int(data[i+1][j]) > currentValue:
                return True
    elif i == 99:
        if j != 0 or j != len(data)-1:
            if int(data[i][j-1]) > currentValue and int(data[i][j+1]) > currentValue and int(data[i-1][j]) > currentValue:
                return True
        elif j == 0:
            if int(data[i][j+1]) > currentValue and int(data[i-1][j]) > currentValue:
                return True
        elif j == len(data) - 1:
            if int(data[i][j-1]) > currentValue and int(data[i-1][j]) > currentValue:
                return True
    return False

for i in range(100):
    str = data[i]
    for j in range(len(str)):
        if ifLow(i,j):
            lowPoints.append(int(data[i][j]))

print(sum(lowPoints)+len(lowPoints))
