engine = open("tres\\engine.txt")


def has_symbol(iline, numindex, numlen):
    symbols = ["*", "=", "/", "@", "$", "%", "&", "#"]
    symbol = False
    if iline == 0:
        cline = engine.readline(iline)
        above = engine.readline(iline)
        pline = above[numindex - 1, numlen + 1]
        if numindex == 0:

            symbol = (cline[numindex + numlen] != ".") or any(substring in pline for substring in symbols)
        elif numindex == len(line):
            symbol = (cline[numindex - 1] != ".")
        else:
            symbol = (cline[numindex + numlen] != ".") or (cline[numindex - 1] != ".")

    return symbol


partsSum = 0
iline = 0
for line in engine:
    i = 0
    consecutive = False
    numberIndex = 0
    for x in line:
        i += 1
        number = ""
        # consecutive numbers
        if x.isnumeric() and consecutive:
            number += x
        # new number
        elif x.isnumeric():
            number = x
            numberIndex = i
            consecutive = True
        # number ended / no number found yet
        if not x.isnumeric:
            consecutive = False
            number = ""
            if len(number) != 0:
                if has_symbol(iline, numberIndex, len(number)):
                    partsSum += int(number)
    iline += 1
print(partsSum)
