file = open("input.txt","r")

data = file.readlines()

eights = 0
ones = 0
fours = 0
sevens = 0

for line in data:
    delim = line.find("|")
    print(delim)
    strOfCodes = line[delim+2:len(line)].strip()
    numbers = strOfCodes.split(" ")
    for num in numbers:
        if len(num) == 2:
            ones+=1
        elif len(num) == 4:
            fours+=1
        elif len(num) == 3:
            sevens+=1
        elif len(num) == 7:
            eights+=1

print(ones+fours+sevens+eights)
