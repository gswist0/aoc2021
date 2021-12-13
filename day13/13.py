import numpy as np
import matplotlib.pyplot as plt

with open("D:\\aoc\day13\input.txt","r") as file:
    lines = file.readlines()

folds = []

lines_copy = lines.copy()

max_x=0
max_y=0

for line in lines_copy:
    if "," in line:
        point_x = int(line.strip().split(",")[0])
        point_y = int(line.strip().split(",")[1])
        if point_y > max_y:
            max_y = point_y
        if point_x > max_x:
            max_x = point_x

board = np.zeros((max_x+1,max_y+1))
for line in lines:
    if "," not in line and line.strip() != "":
        equation = line.strip().split()[2]
        if equation.split("=")[0] == "x":
            folds.append(("x",int(equation.split("=")[1])))
        else:
            folds.append(("y",int(equation.split("=")[1])))
    elif "," in line:
        point_x = int(line.strip().split(",")[0])
        point_y = int(line.strip().split(",")[1])
        board[point_x][point_y] += 1

board = board.transpose()

def fold(board, index, using_x=False):
    if using_x:
        board = board.transpose()
    new_board = np.zeros((len(board)-index-1,len(board[0])))
    old_board_index = index+1
    for i in reversed(list(enumerate(new_board))):
        if old_board_index < len(board):
            new_board[i[0]] = board[i[0]]+board[old_board_index]
        else:
            new_board[i[0]] = board[i[0]]
        old_board_index += 1
    print(new_board)

    if using_x:
        new_board = new_board.transpose()

    return new_board

def count_not_zeros(board):
    result = 0
    for row in board:
        for number in row:
            if number != 0:
                result += 1
    return result

def fold_direction(string):
    if string == "x":
        return True
    else:
        return False

for directive in folds:
    board = fold(board,directive[1],fold_direction(directive[0]))

for row in board:
    for i,value in enumerate(row):
        if value != 0:
            row[i] = 1

plt.imshow(board)
plt.show()