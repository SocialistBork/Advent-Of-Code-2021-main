file = open("input.txt", "r")
data = sorted(map(int, file.readline().split(",")))

def sumOfAllNums(n):
    return int(n*(n+1)/2)

average = round(sum(data)/len(data))

distances = []

for i in range(min(data), max(data)+1):
    distance = 0
    for number in data:
        distance+=sumOfAllNums(abs(number-i))
    distances.append(distance)

print(sumOfAllNums(6))
print(min(distances))
