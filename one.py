file = open("C:\\Users\\Afonso deSousa\\OneDrive - FCT NOVA\\Documents\\Code\\advent_code_23\\calibration.txt")
calibraton = 0

for line in file:
    isFirstNum = True
    firstNum = 0
    lastNum = 0

    for x in line:
        if x.isnumeric() and isFirstNum:
            firstNum = int(x)
            lastNum = int(x)
            isFirstNum = False
        elif x.isnumeric():
            lastNum = int(x)
            
    firstNum += lastNum
    calibration = firstNum

print(calibration)

file.close()