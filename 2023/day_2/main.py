import re
import numpy

def make_game_object(pulls):
    ret_dict={}
    for idx, pull in enumerate(pulls):
        ret_dict[str(idx)] = {}
        colours = pull.split(",")
        for colour in colours:
            if "blue" in colour:
                ret_dict[str(idx)]["blue"] = int(re.findall("[0-9]+",colour)[0])
            elif "red" in colour:
                ret_dict[str(idx)]["red"] = int(re.findall("[0-9]+",colour)[0])
            elif "green" in colour:
                ret_dict[str(idx)]["green"] = int(re.findall("[0-9]+",colour)[0])
    return ret_dict
        

limits = {"red":12,"green":13,"blue":14}
file = open("input.txt","r")
data = file.read().split("\n")

part_1_count = 0
part_2_count = 0
for line in data:
    id = int(re.findall("^Game [0-9]*",line)[0].split(" ")[1])
    pulls = line.split(":")[1].split(";")
    game = make_game_object(pulls)
    valid_game = True
    game_min = {"red":0,"green":0,"blue":0}
    for pull in game:
        for key in game[pull].keys():
            if game[pull][key] > limits[key]:
                valid_game = False
            if game[pull][key] > game_min[key]:
                game_min[key] = game[pull][key]
    if valid_game :
        part_1_count += id
    part_2_count += numpy.prod(list(game_min.values()))
print(part_1_count)
print(part_2_count)