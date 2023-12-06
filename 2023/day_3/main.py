import re

file = open("input.txt","r")
raw_data = file.read()
charter_set=set(raw_data)
char_matrix = raw_data.split("\n")
parity_matrix = [["."]*len(char_matrix[0]) for j in range(len(char_matrix[0]))]
symbols = charter_set - {"0","1","2","3","4","5","6","7","8","9",".","\n"}

def populate_parity(x,y,data=char_matrix,parity=parity_matrix):
    if (0<=x<len(data) and 0<=y<len(data)):
        if (data[y][x].isdigit() and parity[y][x]== "."):
            parity[y][x]=data[y][x]
            populate_parity(x-1,y,data,parity)
            populate_parity(x+1,y,data,parity)
    return

for y ,row in enumerate(char_matrix):
    for x, char in enumerate(row):
        if char in symbols:
            for i in range(-1,2):
                for j in range(-1,2):
                    populate_parity(x+i,y+j)
            if char == "*":
                parity_matrix[y][x]=char
count = 0
for line in parity_matrix:
    numbs = re.findall("[0-9]+","".join(line))
    for number in numbs:
        count += int(number)
    
print(count)

for line in parity_matrix:
    print("".join(line))