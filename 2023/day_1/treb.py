def format_string(raw_string):
    formatted_string = ""
    for idx, charchter in enumerate(raw_string):
        if charchter.isdigit():
            formatted_string+=charchter
        elif  charchter == "z":
            if raw_string[idx:idx+4]=="zero":
                formatted_string+="0"
        elif  charchter == "o":
            if raw_string[idx:idx+3]=="one":
                formatted_string+="1"
        elif  charchter == "t":
            if raw_string[idx:idx+3]=="two":
                formatted_string+="2"
            elif raw_string[idx:idx+5]=="three":
                formatted_string+="3"
        elif  charchter == "f":
            if raw_string[idx:idx+4]=="four":
                formatted_string+="4"
            elif raw_string[idx:idx+4]=="five":
                formatted_string+="5"
        elif  charchter == "s":
            if raw_string[idx:idx+3]=="six":
                formatted_string+="6"
            elif raw_string[idx:idx+5]=="seven":
                formatted_string+="7"
        elif  charchter == "e":
            if raw_string[idx:idx+5]=="eight":
                formatted_string+="8"
        elif  charchter == "n":
            if raw_string[idx:idx+4]=="nine":
                formatted_string+="9"
    return formatted_string


file = open("treb_input.txt","r")

data = file.read().split("\n")
count = 0
for entry in data :
    print(entry)
    numbers = []
    processed = format_string(entry)
    print(processed)
    for  charchter in processed:
        if  charchter.isdigit():
            numbers.append( charchter)
    count += int(numbers[0]+numbers[-1])

print(count)
