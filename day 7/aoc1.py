file = open("simple.txt","r")
data = sorted(map(int, file.readline().split(",")))

print(data)

n = (len(data)-1)//2
if len(data)%2==1:
    median = data[n]
else:
    median = (data[n]+data[n+1])/2

distance = 0
for num in data:
    distance += abs(num-median)

print(distance)
