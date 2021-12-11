f = open("D:\\aoc\day2\input.txt", "r")
horizontal = 0
depth = 0
aim = 0

for line in f.readlines() :
    command = line.split()[0]
    amount = int(line.split()[1])
    if command == "forward" :
        horizontal += amount
        depth += (aim*amount)
    elif command == "up" :
        aim -= amount
    elif command == "down" :
        aim += amount

print(horizontal*depth)


