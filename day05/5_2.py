import numpy as np

with open("D:\\aoc\day5\input.txt","r") as file:
    lines = file.readlines()

board = np.zeros((1000 , 1000))


for line in lines:
    point1 = line.split()[0]
    point2 = line.split()[2]
    x1 = int(point1.split(",")[0])
    y1 = int(point1.split(",")[1])
    x2 = int(point2.split(",")[0])
    y2 = int(point2.split(",")[1])
    if(x1 == x2):
        if(y1>y2):
            range_y = range(y2,y1+1)
        else:
            range_y = range(y1,y2+1)
        for i in range_y:
            board[i][x1] += 1
    elif(y1 == y2):
        if(x1>x2):
            range_x = range(x2,x1+1)
        else:
            range_x = range(x1,x2+1)
        for i in range_x:
            board[y1][i] += 1
    else:
        x = x1
        end_x = x2
        y = y1
        end_y = y2
        while x!=end_x and y!=end_y:
            board[y][x] += 1
            if(x>end_x):
                x -= 1
            else:
                x += 1
            if(y>end_y):
                y -= 1
            else:
                y += 1
        board[y][x] += 1

overlaps = 0
for row in board:
    for number in row:
        if(number>1):
            overlaps += 1

print(overlaps)
        
    


