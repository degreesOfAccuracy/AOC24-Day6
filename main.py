from copy import deepcopy

def check_for_loop(next_pos, original_pos):
    map3 = deepcopy(map1)
    visited = set()
    map3[next_pos[0]][next_pos[1]] = "#"
    pos = deepcopy(original_pos)
    dir = (-1, 0)
    while True:
        next_pos = (pos[0] + dir[0], pos[1] + dir[1])
        if any([c < 0 for c in next_pos]) or any(c >= s for c, s in zip(next_pos, map_size)):
            return False
        elif map3[next_pos[0]][next_pos[1]] == "#":
            dir = (dir[1], -dir[0])
        else:
            pos = next_pos
            if (pos, dir) in visited:
                return True
            visited.add((pos, dir))

with open("input.txt") as file:
    map1 = [list(line.strip()) for line in file.readlines()]
map2 = deepcopy(map1)
map_size = [len(map1), len(map1[0])]

pos = [(y, line.index("^")) for y, line in enumerate(map1) if "^" in line][0]
original_pos = deepcopy(pos)
dir = (-1, 0)

counter = 0
while True:
    map1[pos[0]][pos[1]] = "X"
    counter += 1
    next_pos = (pos[0] + dir[0], pos[1] + dir[1])
    if any([c < 0 for c in next_pos]) or any(c >= s for c, s in zip(next_pos, map_size)):
        print(sum([sum([c == "X" for c in row]) for row in map1]))
        print(sum([sum([c == "O" for c in row]) for row in map2]))
        break
    elif map1[next_pos[0]][next_pos[1]] == "#":
        dir = (dir[1], -dir[0])
        counter -= 1
    else:
        if next_pos != original_pos and check_for_loop(next_pos, original_pos):
            map2[next_pos[0]][next_pos[1]] = "O"
        pos = next_pos
print(counter)
