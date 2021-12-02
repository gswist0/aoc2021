f = open("D:\\aoc\day1\input.txt", "r")
counter = 0

windows = []

prev1 = 0
prev2 = 0

for line in f.readlines() :
    start_value = int(line.strip())
    value = start_value
    value += prev1
    value += prev2
    if(prev1!=0 and prev2!=0) :
        windows.append(value)
    prev1=prev2
    prev2=start_value

prev_window = 30000

for window in windows :
    print(str(window) + " " + str(prev_window))
    if(window>prev_window) :
        counter+=1
    prev_window = window
    
print(counter)