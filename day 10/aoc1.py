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

for line in data:
    illgalChar = findIllgalChar(line)
    if illgalChar == ")":
        points += 3
    elif illgalChar == "]":
        points+=57
    elif illgalChar == "}":
        points+=1197
    elif illgalChar == ">":
        points+= 25137

print(points)
