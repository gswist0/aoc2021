with open("D:\\aoc\day8\input.txt","r") as file:
    lines = file.readlines()

final_result = 0
for line in lines:
    input = line.split("|")[0]
    input_split = input.split()
    digits = [""]*10
    uh = ""
    mh = ""
    lh = ""
    ruv = ""
    rlv = ""
    luv = ""
    llv = ""
    len6 = []
    len5 = []
    for value in input_split:
        if(len(value) == 2):
            digits[1] = value
        elif(len(value) == 3):
            digits[7] = value
        elif(len(value) == 4):
            digits[4] = value
        elif(len(value) == 7):
            digits[8] = value
        elif(len(value) == 5):
            len5.append(value)
        else:
            len6.append(value)
    for letter in digits[7]:
        if letter not in digits[1]:
            uh = letter
    for value in len6:
        for letter in digits[1]:
            if letter not in value:
                ruv = letter
                digits[6] = value
                len6.remove(value)
    for letter in digits[1]:
        if letter != ruv:
            rlv = letter
    for value in len5:
        if ruv not in value:
            digits[5] = value
            len5.remove(value)
    for value in len5:
        if rlv not in value:
            digits[2] = value
            len5.remove(value)
    digits[3] = len5[0]
    for letter in digits[6]:
        if letter not in digits[5]:
            llv = letter
    for letter in digits[4]:
        if letter not in digits[1] and letter in digits[3]:
            mh = letter
    for value in len6:
        if mh not in value:
            digits[0] = value
            len6.remove(value)
    digits[9] = len6[0]

    for i in range(len(digits)):
        digits[i] = "".join(sorted(digits[i]))

    result = ""
    output = line.split("|")[1]
    output_split = output.split()
    
    for i in range(len(output_split)):
        output_split[i] = "".join(sorted(output_split[i]))
    for value in output_split:
        result += str(digits.index(value))
    final_result += (int(result))

print(final_result)