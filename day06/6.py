with open("D:\\aoc\day6\input.txt","r") as file:
    fishes = list(map(lambda x: int(x),file.readline().split(",")))

fishes_with_timer = [0,0,0,0,0,0,0,0,0]

for n,i in enumerate(fishes):
    fishes_with_timer[fishes[n]] += 1

def sim(days=80):
    for _ in range(days):
        ex0 = 0
        for n,i in enumerate(fishes_with_timer):
            if n == 0:
                ex0 = fishes_with_timer[n]
            else:
                fishes_with_timer[n-1] = fishes_with_timer[n]
            fishes_with_timer[n] = 0
        fishes_with_timer[6] += ex0
        fishes_with_timer[8] += ex0
                


sim(256)
print(sum(fishes_with_timer))