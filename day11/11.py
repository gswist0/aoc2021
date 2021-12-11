import numpy as np

with open("D:\\aoc\day11\input.txt","r") as file:
    lines = file.readlines()


def flash(octopuses,i,j,alreadyFlashed):
    if octopuses[i][j] > 9 and alreadyFlashed[i][j] == False:
        alreadyFlashed[i][j] = True
        if(i != 0 and j != 0):
            octopuses[i-1][j-1] += 1
            result = flash(octopuses,i-1,j-1,alreadyFlashed)
            octopuses = result[0]
            alreadyFlashed = result[1]
        if(i != 0 and j != len(octopuses[i])-1):
            octopuses[i-1][j+1] += 1
            result = flash(octopuses,i-1,j+1,alreadyFlashed)
            octopuses = result[0]
            alreadyFlashed = result[1]
        if(i != 0):
            octopuses[i-1][j] += 1
            result = flash(octopuses,i-1,j,alreadyFlashed)
            octopuses = result[0]
            alreadyFlashed = result[1]
        if(j != len(octopuses[i])-1):
            octopuses[i][j+1] += 1
            result = flash(octopuses,i,j+1,alreadyFlashed)
            octopuses = result[0]
            alreadyFlashed = result[1]
        if(i != len(octopuses)-1 and j != len(octopuses[i])-1):
            octopuses[i+1][j+1] += 1
            result = flash(octopuses,i+1,j+1,alreadyFlashed)
            octopuses = result[0]
            alreadyFlashed = result[1]
        if(i != len(octopuses)-1):
            octopuses[i+1][j] += 1
            result = flash(octopuses,i+1,j,alreadyFlashed)
            octopuses = result[0]
            alreadyFlashed = result[1]
        if(i != len(octopuses)-1 and j != 0):
            octopuses[i+1][j-1] += 1
            result = flash(octopuses,i+1,j-1,alreadyFlashed)
            octopuses = result[0]
            alreadyFlashed = result[1]
        if(j != 0):
            octopuses[i][j-1] += 1
            result = flash(octopuses,i,j-1,alreadyFlashed)
            octopuses = result[0]
            alreadyFlashed = result[1]
    return octopuses, alreadyFlashed

def simulate_flashes(octopuses,simulationsCount=100):
    flashes = 0
    synchronizedSim = 0
    for sim in range(simulationsCount):
        alreadyFlashed = np.zeros((10,10),dtype=bool)
        for i in range(len(octopuses)):
            for j in range(len(octopuses[i])):
                octopuses[i][j] += 1
                result = flash(octopuses,i,j,alreadyFlashed)
                octopuses = result[0]
                alreadyFlashed = result[1]

        flashesThisSim = 0
        for i in range(len(octopuses)):
            for j in range(len(octopuses[i])):
                if octopuses[i][j] > 9:
                    octopuses[i][j] = 0
                    flashes +=1
                    flashesThisSim += 1

        if(flashesThisSim == 100 and synchronizedSim == 0):
            synchronizedSim = sim+1
        
    return flashes,synchronizedSim

octopuses = []
octopusesPart2 = []

for line in lines:
    octopuses.append([int(i) for i in list(line.strip())])
    octopusesPart2.append([int(i) for i in list(line.strip())])



simulation = simulate_flashes(octopuses)
simulationPart2 = simulate_flashes(octopusesPart2,1000)

print(simulation[0])
print(simulationPart2[1])