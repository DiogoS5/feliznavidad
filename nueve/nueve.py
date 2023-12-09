import re  

input = open(r"input.txt", "r")

og_lines = []
for line in input:
    og_lines.append(line.strip().split(" "))

result = 0
for line in og_lines:
    line = [int(i)  for i in line] #convert to ints
    pyramid = []
    pyramid.append(line)
    for p in range(len(line)):
        deltas = []
        for i in range(1, len(pyramid[p])):
            deltas.append(pyramid[p][i]-pyramid[p][i-1])
        if all([i == 0 for i in deltas]):
            break
        pyramid.append(deltas)

    for p in range(len(pyramid)-1, 0, -1):
        pyramid[p-1].append(pyramid[p][-1]+pyramid[p-1][-1])

    result += pyramid[0][-1]

print(result)