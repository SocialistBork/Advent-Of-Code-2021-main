def fineMostCommon(list, pos):
    ones = 0
    zeros = 0
    for num in list:
        if int(num[0][pos]) == 1:
            ones+=1
        else:
            zeros+=1
    if ones>zeros or ones==zeros:
        return 1
    else:
        return 0

def getOxygen(num):
    print("oxugen")
    oxygen = list(num)
    i = 0
    while i < 12:
        mostCommon = fineMostCommon(oxygen,i)
        o2copy = list(oxygen)
        for data in o2copy:
            if data[0][i] != "" and int(data[0][i]) != mostCommon:
                oxygen.remove(data)
        i+=1
    return oxygen[0][0]

def getCO2(num):
    print("CUM")
    co2 = list(num)
    i = 0
    while i < 12 and len(co2) > 1:
        mostCommon = fineMostCommon(co2,i)
        co2copy = list(co2)
        for data in co2copy:
            if data[0][i] != "" and int(data[0][i]) == mostCommon:
                co2.remove(data)
        i+=1
    return co2[0][0]

file = open("list.txt","r")
numbers = file.readlines()

for i in range(len(numbers)):
    numbers[i] = numbers[i].strip().split("\n")

print(int(getOxygen(numbers),2)*int(getCO2(numbers),2
