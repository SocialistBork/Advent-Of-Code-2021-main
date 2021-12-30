file = open("list.txt","r")
horizontal = 0
depth = 0
aim = 0

for line in file:
    parts = line.split(" ")
    number = int(parts[1])
    if parts[0] == "down":
        aim += number
    elif parts[0] == "up":
        aim -= number
    elif parts[0] == "forward":
        horizontal += number
        depth += aim*number

print(horizontal*depth)
