import re


input = open(r"cuatro\test.txt", "r")
result = 0

while hasCards:
    


def checkForHits(keys, scratched):
    score = 0
    for scratch in scratched:
        if scratch in keys:
            score += 1

    return score

cardId = 0
for card in  input:
    #TODO: Sousa exbrains y work
    #removes "Card [i]: "
    match = re.search(r'Card (\d+):', card)
    if match:
        id = match.group(1) #store id
        card = card.replace(match.group(0), "") #remove "Card ...:"
    

    numbers = card.split("|")

    #stores each card key in a list
    card_keys = []
    key = ""
    i = 0
    for x in numbers[0]:
        if x != " ":
            key += x

        else:
            if len(key) > 0:
                card_keys.append(key)
                key = ""
        i += 1

    #stores each card scratched number in a list
    card_scratch = []
    scratched = ""
    i = 0
    for x in numbers[1]:
        if x != " " and x != "\n":
            scratched += x
            if i == len(numbers[1]) - 1:
                card_scratch.append(scratched)
        else:    
            if len(scratched) > 0:
                card_scratch.append(scratched)
                scratched = ""

        i +=1

    result += checkForHits(card_keys, card_scratch) + 1

print(result)
