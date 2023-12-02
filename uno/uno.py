file = open("input.txt")
calibration = 0

for line in file:
    isFirstNum = True
    for x in line:
        if x.isnumeric() and isFirstNum:
            firstNum = x
            lastNum = x
            isFirstNum = False
        elif x.isnumeric():
            lastNum = x

    firstNum += lastNum
    calibration += int(firstNum)

print(calibration)

file.close()