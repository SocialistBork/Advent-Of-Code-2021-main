file = open("list.txt", "r")

horizontal = 0
depth = 0

for line in file:
    parts = line.split(" ")
    number = int(parts[1])
    if parts[0] == "forward":
        horizontal += number
    elif parts[0] == "down":
        depth += number
    elif parts[0] == "up":
        depth -= number

print(horizontal * depth)
