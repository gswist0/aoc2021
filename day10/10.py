with open("D:\\aoc\day10\input.txt","r") as file:
    lines = file.readlines()

def corrupted_points(line):
    opening_signs = ["(","{","<","["]
    closing_signs = [")","}",">","]"]
    stack = []
    for sign in line.strip():
        if(sign in opening_signs):
            stack.append(closing_signs[opening_signs.index(sign)])
        elif(sign != stack.pop()):
            if(sign == ")"):
                return 3
            elif(sign == "]"):
                return 57
            elif(sign == "}"):
                return 1197
            else:
                return 25137
    return 0

def autocomplete(line):
    opening_signs = ["(","{","<","["]
    closing_signs = [")","}",">","]"]
    stack = []
    for sign in line.strip():
        if(sign in opening_signs):
            stack.append(closing_signs[opening_signs.index(sign)])
        else:
            stack.pop()

    stack.reverse()

    score = 0
    for sign in stack:
        score *= 5
        if(sign == ")"):
            score += 1
        elif(sign == "]"):
            score += 2
        elif(sign == "}"):
            score += 3
        else:
            score += 4
    return score

completion_scores = []

error_score = 0 
for line in lines:
    score = corrupted_points(line)
    error_score += score
    if(score == 0):
        completion_scores.append(autocomplete(line))

print(error_score)
print(sorted(completion_scores)[len(completion_scores)//2])