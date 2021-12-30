file = open("list.txt", "r")
number = file.readlines()

mcb = []
lcb = []

i = 0
while i < 12:
    ones = 0
    zeros = 0
    for line in number:
        if int(line[i]) == 1:
            ones += 1
        else:
            zeros += 1
    if ones > zeros:
        mcb.append(1)
        lcb.append(0)
    else:
        mcb.append(0)
        lcb.append(1)
    i+=1


def joinTogether(binary):
    bin = ""
    for num in binary:
        bin = bin + str(num)
    return bin

mb = joinTogether(mcb)
lb = joinTogether(lcb)

print(int(mb,2))
print(int(lb,2))
print(int(mb,2)*int(lb,2))
