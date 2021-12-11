with open("D:\\aoc\day7\input.txt","r") as file:
    crabs = list(map(int,file.readline().split(",")))

def calculate_fuel(iq200 = False):
    least_fuel = pow(max(crabs)*len(crabs),2)
    for position in range(min(crabs),max(crabs)):
        fuel_used = 0
        for crab in crabs:
            distance = abs(crab-position)
            if not iq200:
                fuel_used += distance
            else:
                fuel_used += (2*distance + (distance-1) * (-1))*distance/2
        if fuel_used < least_fuel:
            least_fuel = fuel_used
    return int(least_fuel)

print(calculate_fuel())
print(calculate_fuel(True))