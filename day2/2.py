f = open("D:\\aoc\day2\input.txt", "r")
horizontal = 0
depth = 0

for line in f.readlines() :
    command = line.split()[0]
    amount = int(line.split()[1])
    if command == "forward" :
        horizontal += amount
    elif command == "up" :
        depth -= amount
    elif command == "down" :
        depth += amount

print(horizontal*depth)


