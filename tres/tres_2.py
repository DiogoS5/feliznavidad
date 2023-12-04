#72968709 too low
engine = open("C:\\Users\\Afonso deSousa\\OneDrive - FCT NOVA\\Documents\\Code\\feliznavidad\\tres\\engine.txt", "r")

matrix = []

#any(substring in linha for substring in symbols) -> bool

for line in engine:
    matrix.append(list(line.strip()))

engine.close()


def readLine(line, index):
    reading = line[index]
    if index > 0:
        reading = line[index-1] + reading
    if index < len(line):
        reading = reading + line[index+1]

    x = index - 2
    if line[index - 1].isnumeric():
        while x >= 0 and line[x].isnumeric():
            reading = line[x] + reading
            x -= 1

    x = index + 2
    if line[index + 1].isnumeric():
        while x < len(line) and line[x].isnumeric():
            reading += line[x]
            x += 1
    
    reading = reading.split(".")
    reading = [str for str in reading if str]
    return reading
        
def hasAdjacent(i, iline):
    num = ""
    numbers = []
    if i > 0:
        #check adjacent to the left
        if matrix[iline][i - 1].isnumeric():
            index = i - 1
            while index >= 0 and matrix[iline][index].isnumeric():
                num = matrix[iline][index] + num
                index -= 1
        if num != "":
            numbers.append(num)

    num = ""
    if i + 1 < (len(line)):
        #check adjacent to the right
        if matrix[iline][i + 1].isnumeric():
            index = i + 1 
            while index < len(matrix[iline]) and matrix[iline][index].isnumeric():
                num += matrix[iline][index]
                index += 1
        if num != "":
            numbers.append(num)
    
    if iline > 0:
        numbers.extend(readLine(matrix[iline - 1], i))
    if iline < len(matrix)-1:
        numbers.extend(readLine(matrix[iline + 1], i))
    print(numbers)
    return numbers


result = 0
iline = 0
for line in matrix:
    number = ""
    i = 0
    for x in line:
        if x == "*":
            numbers = hasAdjacent(i, iline)
            if len(numbers) == 2:
                prod = int(numbers[0]) * int(numbers[1])
                result += prod
        i += 1
    iline += 1

print(result)

#488618 low