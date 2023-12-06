import re

input = open(r"input.txt", "r")

content = input.readlines()

times = re.findall(r'\d+', content[0])
time = ""
for t in times:
    time += t
time = int(time)

distances = re.findall(r'\d+', content[1])
targ_distance = ""
for d in distances:
    targ_distance += d
targ_distance = int(targ_distance)

print(time)
print(targ_distance)

possibilites = 0
for t in range(time):
    distance = (time-t)*t
    if distance > targ_distance:
        possibilites += 1

print(possibilites)