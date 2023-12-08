input = open(r"input.txt", "r")

instructions = list(input.readline().strip())

input.readline() #skip blank line

map = {}

for line in input:
    key = line[0:3]
    map[key] = [line[7:10], line[12:15]]

steps = 0
finished = False
current = "AAA"
while not finished:
    for instruction in instructions: 
        steps += 1
        if instruction == "L":
            current = map[current][0]
        elif instruction == "R":
            current = map[current][1]
        if current == "ZZZ":
            finished = True
            break
print(steps)
        
    

