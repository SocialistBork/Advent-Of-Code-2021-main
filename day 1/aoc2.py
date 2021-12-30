file = open("list.txt", "r")
old = file.readlines()
inc = 0
dec = 0

everyThree = []

i = 0
while i+2 < len(old):
    everyThree.append(int(old[i])+int(old[i+1])+int(old[i+2]))
    i += 1

j = 0
while j+1 < len(everyThree):
    if everyThree[j+1] > everyThree[j]:
        inc += 1
    elif everyThree[j+1] < everyThree[j]:
        dec += 1
    j += 1

print(inc)
