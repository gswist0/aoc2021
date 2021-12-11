import numpy as np

with open("D:\\aoc\day9\input.txt","r") as file:
    lines = file.readlines()

is_part_of_basin = np.zeros((len(lines),len(lines[0])),dtype=bool)

task1 = 0

basin_size = 0
basin_sizes = []

def isLowPoint(i,j):
    line = lines[i].strip()
    adjacent = [10,10,10,10]
    is_low_point = True
    if(j != 0):
        adjacent[3] = int(line[j-1])
    if(i != 0):
        adjacent[0] = int(lines[i-1][j])
    if(j != len(line.strip())-1):
        adjacent[1] = int(line[j+1])
    if(i != len(lines)-1):
        adjacent[2] = int(lines[i+1][j])
    for k,neighbour in enumerate(adjacent):
        if(int(point) >= neighbour):
            is_low_point = False
    return is_low_point

def calculateBasin(i,j,ignore=4):
    global basin_size
    if(int(lines[i][j]) != 9 and is_part_of_basin[i][j] == False):
        basin_size += 1
        is_part_of_basin[i][j] = True
        if(ignore != 2 and i!=len(lines)-1):
            calculateBasin(i+1,j,ignore=0)
        if(ignore != 0 and i!=0):
            calculateBasin(i-1,j,ignore=2)
        if(ignore != 1 and j!=len(lines[0].strip())-1):
            calculateBasin(i,j+1,ignore=3)
        if(ignore != 3 and j!=0):
            calculateBasin(i,j-1,ignore=1)       


for i, line in enumerate(lines):
    for j, point in enumerate(line.strip()):
        basin_size = 0
        if(isLowPoint(i,j)):
            task1 += (int(point) + 1)
            calculateBasin(i,j)
            basin_sizes.append(basin_size)

print(task1)
biggest = []
for i in range(3):
    biggest_value = 0
    for value in basin_sizes:
        if(value>biggest_value):
            biggest_value = value
    basin_sizes.remove(biggest_value)
    biggest.append(biggest_value)

print(np.prod(biggest))