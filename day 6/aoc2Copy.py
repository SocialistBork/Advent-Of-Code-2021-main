file = open("input.txt", "r")
strAge = file.readline().split(",")

def printList(arr):
    print(arr)

age = []
for num in strAge:
    age.append(int(num))

numberOfAges = [0]*9

for number in age:
    numberOfAges[number]+=1

for i in range(256):
    nextGen = numberOfAges[1:]+numberOfAges[:1]
    nextGen[6] += nextGen[8]
    numberOfAges = list(nextGen)

count = 0
for val in numberOfAges:
    count+=val

print(sum(numberOfAges))
