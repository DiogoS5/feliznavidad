#53527 too high
fin = open("input.txt", "rt")

numbers = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}

calibration = 0
for line in fin:
    isFirstNum = True
    firstNum = 0
    lastNum = 0 

    i = 0
    first = len(line)
    last = 0
    for x in line:
        if x.isnumeric() and isFirstNum:
            firstNum = x
            lastNum = x
            isFirstNum = False
            first = i
        if x.isnumeric():
            lastNum = x
            print(last)
            last = i
        i += 1   
        
    for n in numbers:
        try:
            index = line.index(n)    
        except ValueError:
            continue  

        if 0 <= index < first:
            first = index
            firstNum = numbers.get(n)

        try:
            lastindex = line.rindex(n)
        except ValueError:
            continue 
        
        if last <= lastindex:
            last = lastindex
            lastNum = numbers.get(n)

    
    firstNum += lastNum
    calibration += int(firstNum)

print(lastindex)
print(calibration)




    
    
