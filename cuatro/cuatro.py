import re

input = open(r"input.txt", "r")

total = 0
matches = []  # [0] = matches, [1] = n_cards
i = 0
for line in input:
    #readings
    winners = line.split("|")[0]
    winners = winners.split(":")[1]
    winners = re.findall(r'\d+', winners)
    card = line.split("|")[1]
    card = re.findall(r'\d+', card)

    matches.append([0, 1])

    for c in card:
        if c in winners:
            matches[i][0] += 1

    i += 1

for i in range(len(matches)):
    for r in range(matches[i][0]):
        matches[i+1+r][1] += matches[i][1]

for i in range(len(matches)):
    total += matches[i][1]

print(total)