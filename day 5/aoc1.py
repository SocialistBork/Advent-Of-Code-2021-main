file = open("input.txt", "r")
data = file.readlines()

rows, cols = (1000, 1000)
arr=[]
for i in range(rows):
    col = []
    for j in range(cols):
        col.append(0)
    arr.append(col)

def printBoard(array):
    for col in array:
        print(col)

for coords in data:
    twoCoords = coords.strip().split(" -> ")
    x1 = int(twoCoords[0][0:twoCoords[0].find(",")])
    x2 = int(twoCoords[1][0:twoCoords[1].find(",")])
    y1 = int(twoCoords[0][twoCoords[0].find(",")+1:len(twoCoords[0])])
    y2 = int(twoCoords[1][twoCoords[1].find(",")+1:len(twoCoords[1])])
    print(str(x1)+","+str(y1))
    print(str(x2)+" "+str(y2))
    if x1 == x2:
        for i in range(min(y1,y2),max(y1,y2)+1):
            arr[i][x1]+=1
            i+=1
    elif y1 == y2:
        for i in range(min(x1,x2),max(x1,x2)+1):
            arr[y1][i] += 1
            i+=1

#printBoard(arr)

count = 0
for i in range(1000):
    for j in range(1000):
        if arr[i][j] > 1:
            count+=1

print(count)
