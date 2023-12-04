#2554 too low
import re

input = open(r"dos\test.txt", "r")

result = 0

for game in input:
    print(game)
    match = re.search(r'Game (\d+):', game)
    if match:
        id = match.group(1) #store id
        game = game.replace(match.group(0), "") #remove "Game ...:"

    plays = re.split(r";", game)

    valid = True

    for play in plays:
        grabs = re.split(r", ", play) # split by spaces

        grabs[0] = grabs[0][1:]
        grabs[-1] = grabs[-1].replace("\n", "") # fix the assignment

        count = {"red": 0, "green": 0, "blue": 0}

        for grab in grabs:
            grab = grab.split() # split by whitespace
            count[grab[1]] = int(grab[0])
        
        print(count)
        if count.get("red") > 12 or count.get("green") > 13 or count.get("blue") > 14:
            valid = False
            print(valid)
            break
    
    if valid:
         result += int(id)
            
print(result)