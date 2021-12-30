file = open("input.txt","r")

data = file.readlines()

listOfNums = []

def findInCommon(str1, str2):
    count = 0
    for i in range(len(str1)):
        for j in range(len(str2)):
            if str1[i] == str2[j]:
                count+=1
    return count

def findKey(strIn):
    str = strIn.split(" ")
    arr = [0]*10
    for num in str:
        if len(num) == 2:
            arr[1] = num
        elif len(num) == 4:
            arr[4] = num
        elif len(num) == 3:
            arr[7] = num
        elif len(num) == 7:
            arr[8] = num
    for num in str:
        if len(num) == 6:
            if findInCommon(arr[1],num) == 1:
                arr[6] = num
            elif findInCommon(arr[4],num) != 4:
                arr[0] = num
            else:
                arr[9] = num
    for num in str:
        if len(num) == 5:
            if findInCommon(arr[1],num) == 2:
                arr[3] = num
            elif findInCommon(arr[6], num) == 4:
                arr[2] = num
            else:
                arr[5] = num
    return arr


for line in data:
    delim = line.find("|")
    strOfCodes = line[0:delim - 1]
    key = findKey(strOfCodes)
    strOfNumber = line[delim + 2:len(line)].strip()
    numbers = strOfNumber.split(" ")

    digits = []

    for num in numbers:
        for i in range(10):
            if sorted(num) == sorted(key[i]):
                digits.append(str(i))
                break
    listOfNums.append(int("".join(digits)))

print(sum(listOfNums))
