import re

input = open("input.txt", "r")

first_line = input.readline()
seeds = re.findall(r"\d+", first_line)
seeds = [int(s) for s in seeds]
#print(seeds)

changed = [0 for i in range(len(seeds))]
for line in input:
    stuff = re.findall(r"\d+", line)
    #print(f'line: {stuff}')
    if stuff != []:
        stuff = [int(s) for s in stuff]
        for i in range(len(seeds)):
            if changed[i] == 0 and seeds[i] in range(stuff[1], stuff[1]+stuff[2]):
                seeds[i] += stuff[0]-stuff[1]
                changed[i] = 1
    else:
        changed = [0 for i in range(len(changed))]
        #print(changed)
    
    #print(seeds)

print(min(seeds))
input.close()