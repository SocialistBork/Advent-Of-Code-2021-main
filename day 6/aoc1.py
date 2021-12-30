file = open("input.txt", "r")
strAge = file.readline().split(",")

def printList(arr):
    print(arr)

age = []
for num in strAge:
    age.append(int(num))

for i in range(80):
    nextGen = list(age)
    for j in range(len(age)):
        if age[j] == 0:
            nextGen[j] = 6
            nextGen.append(8)
        else:
            nextGen[j]-=1
    age = list(nextGen)


print(len(age))
