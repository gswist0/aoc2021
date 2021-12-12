
with open("D:\\aoc\day12\input.txt","r") as file:
    lines = file.readlines()


nodes = {}


for line in lines:
    line = line.strip()
    left_node = line.split("-")[0]
    right_node = line.split("-")[1]
    if left_node in nodes.keys():
        nodes[left_node].append(right_node)
    else:
        nodes[left_node] = [right_node]
    if right_node in nodes.keys():
        nodes[right_node].append(left_node)
    else:
        nodes[right_node] = [left_node]

def wayfinder(nodes,part2=False):
    if not part2:
        running_paths = [["start"]]
    else:
        running_paths = [(["start"],True)]
    complete_paths = []

    while running_paths:
        if not part2:
            current_path = running_paths.pop()
        else:
            current_path,visited_twice = running_paths.pop()
        furthest_cave = current_path[-1]
        neighbors = nodes[furthest_cave]
        for neighbor in neighbors:
            if not part2:
                if neighbor == "end":
                    complete_paths.append(current_path + [neighbor])
                elif neighbor.isupper() or neighbor not in current_path:
                    running_paths.append(current_path + [neighbor])
            else:
                if neighbor == "end":
                    complete_paths.append((current_path + [neighbor],visited_twice))
                elif neighbor == "start":
                    continue
                elif neighbor.isupper() or neighbor not in current_path:
                    running_paths.append((current_path + [neighbor],visited_twice))
                elif visited_twice:
                    running_paths.append((current_path + [neighbor],False))
    return len(complete_paths)

print(wayfinder(nodes))
print(wayfinder(nodes,True))