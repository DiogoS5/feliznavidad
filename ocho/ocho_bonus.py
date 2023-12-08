from math import lcm

input = open(r"input.txt", "r")

instructions = list(input.readline().strip())

input.readline() #skip blank line

map = {}

for line in input:
    key = line[0:3]
    map[key] = [line[7:10], line[12:15]]

steps = 0
current = []
steps = []

for key in map:
    if key[-1] == "A":
        current.append(key)

steps = [0 for i in range(len(current))]
finished = [False for i in range(len(current))]

for i in range(len(current)):
    while not finished[i]:
        for instruction in instructions:
            steps[i] += 1
        #print(instruction)
            if instruction == "L":
                current[i] = map[current[i]][0]
            elif instruction == "R":
                current[i] = map[current[i]][1]
        #print(current)

            if current[i][-1] == "Z":
                finished[i] = True
                break;
print(steps)

lcm_value = steps[0]
for number in steps[1:]:
    lcm_value = lcm(lcm_value, number)
print(lcm_value)
        
    
        
    

