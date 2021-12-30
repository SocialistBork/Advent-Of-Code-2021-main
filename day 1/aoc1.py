file = open("list.txt", "r")
inc = 0
dec = 0

previous = int(file.readline())
while file:
  next = (file.readline())
  if(next == ""):
      break
  if int(next) > previous:
      inc += 1
  elif int(next) < previous:
      dec += 1
  previous = int(next)

print(dec)
print(inc)
