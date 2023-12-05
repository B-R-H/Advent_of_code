file = "input.txt"

data = open(file,"r")

input = data.read()

up = input.count('(')

down = input.count(')')

print("going up "+str(up))
print("going down "+str(down))
print("final floor = "+str(up-down))