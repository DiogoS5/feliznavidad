import re

input = open(r"dos\input.txt", "r")

result = 0

for game in input:
    match = re.search(r'Game (\d+):', game)
    if match:
        id = match.group(1) #store id
        game = game.replace(match.group(0), "") #remove "Game ...:"

    plays = re.split(r";", game)

    valid = True

    max_count = {"red": 0, "green": 0, "blue": 0}

    for play in plays:
        grabs = re.split(r", ", play) # split by spaces

        grabs[0] = grabs[0][1:]
        grabs[-1] = grabs[-1].replace("\n", "") # fix the assignment

        for grab in grabs:
            grab = grab.split() # split by whitespace
            
            if int(grab[0]) > max_count[grab[1]]:
                max_count[grab[1]] = int(grab[0])
    
    power = max_count["red"]*max_count["green"]*max_count["blue"]
    result += power

            
print(result)