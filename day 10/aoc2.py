file = open("input.txt","r")

dataStr = file.readlines()

data = []
for line in dataStr:
    data.append(line.strip())

points = 0

def findIllgalChar(strIn):
    characters = list(strIn)
    open = []

    for char in characters:
        if char == "(" or char == "<" or char == "{" or char == "[":
            open.append(char)
        elif char == ")" or char == ">" or char == "}" or char == "]":
            if open[-1] == "(" and char != ")":
                return char
            elif open[-1] == "<" and char != ">":
                return char
            if open[-1] == "{" and char != "}":
                return char
            elif open[-1] == "[" and char != "]":
                return char
            else:
                open.pop()
    return "."

def completeEndAndCalc(strIn):
    characters = list(strIn)

    open = []
    closed = []

    for char in characters:
        if char == "(" or char == "<" or char == "{" or char == "[":
            open.append(char)
        elif char == ")" or char == ">" or char == "}" or char == "]":
            open.pop()

    for char in reversed(open):
        if char == "(":
            closed.append(")")
        elif char == "<":
            closed.append(">")
        if char == "{":
            closed.append("}")
        elif char == "[":
            closed.append("]")
    score = 0

    for char in closed:
        if char == ")":
            score = score*5 + 1
        elif char == ">":
            score = score*5 + 4
        if char == "}":
            score = score*5 + 3
        elif char == "]":
            score = score*5 + 2

    return score
incomplete = []

for line in data:
    illgalChar = findIllgalChar(line)
    if illgalChar == ".":
        incomplete.append(line)

totalPoints = []

for line in incomplete:
    totalPoints.append(completeEndAndCalc(line))

print(sorted(totalPoints)[int(len(totalPoints)/2)])
