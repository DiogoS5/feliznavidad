
engine = open("tres\\input_sosa.txt", "r")

matrix = []
symbols = ["*", "=", "/", "@", "$", "%", "&", "#", "+", "-"]

#any(substring in linha for substring in symbols) -> bool

for line in engine:
    matrix.append(list(line.strip()))

engine.close()

def hasAdjacent(numIndex, iline, numlen):
    if numIndex > 0:
        range_start = numIndex - 1
        #check adjacent to the left
        if matrix[iline][numIndex - 1] in symbols:
            return True
    else:
        range_start = numIndex
    
    if numIndex + numlen < (len(line)):    
        range_end = numIndex + numlen + 1
        #check adjacent to the right
        if matrix[iline][numIndex + numlen] in symbols:
            return True
    else:
        range_end = numIndex + numlen
    
    if iline > 0: 
        for i in range(range_start, range_end):
            if matrix[iline-1][i] in symbols:
                return True
    if iline < len(matrix)-1:
        for i in range(range_start, range_end):
            if matrix[iline+1][i] in symbols:
                return True
            
    return False


result = 0
iline = 0
for line in matrix:
    consecutive = False
    number = ""
    i = 0
    for x in line:
        if x.isnumeric() and consecutive:
            number += x
        elif x.isnumeric():
            number = x
            consecutive = True
            numIndex = i
        if not x.isnumeric() or i == len(line) - 1:
            consecutive = False
            if len(number) > 0:
                if hasAdjacent(numIndex, iline, len(number)):
                    result += int(number)
            number = ""   
        i += 1
    iline += 1

print(result)

#488618 low