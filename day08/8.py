with open("D:\\aoc\day8\input.txt","r") as file:
    lines = file.readlines()

task1 = 0

for line in lines:
    output = line.split("|")[1]
    for value in output.split():
        if(len(value) == 2 or len(value) == 3 or len(value) == 4 or len(value) == 7):
            task1 += 1

print(task1)