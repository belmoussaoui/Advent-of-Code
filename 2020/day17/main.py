import re
import itertools

def parser():
    file = open("data.txt", "r")
    lines = file.readlines()
    data = {}
    for i in range(len(lines)):
        line = lines[i].strip()
        for j in range(len(line)):
            value = line[j]
            if value == "#":
                key = key_pos(j, i, 0, 0)
                data[key] = 3
    return data

def key_pos(x, y, z, w=0):
    return str(x) + " " + str(y) + " " + str(z) + " " + str(w)

def part1():
    pocket = parser()
    max_cycles = 6
    for cycle in range(max_cycles):
        new_pocket = {}
        for key, value in pocket.items():
            x, y, z, w = [int(number) for number in re.search("(.*) (.*) (.*) (.*)", key).groups()]
            rules(x, y, z, pocket, new_pocket)
        remove_invalid(new_pocket)
        #pretty_print(cycle, new_pocket)
        pocket = new_pocket
    print(len(pocket))

def rules(x, y, z, pocket, new_pocket):
    """
        - If a cube is active and exactly 2 or 3 of its neighbors are also active, the cube remains active.
        Otherwise, the cube becomes inactive.
        - If a cube is inactive but exactly 3 of its neighbors are active, the cube becomes active.
        Otherwise, the cube remains inactive.
    """
    neighbors = 0
    active = 3
    for comb in itertools.product([-1, 0, 1], repeat=3):
        new_x, new_y, new_z = x + comb[0], y + comb[1], z + comb[2]
        if not comb == (0, 0, 0):
            key = key_pos(new_x, new_y, new_z)
            if pocket.get(key, 0):
                neighbors += 1
            else:
                if key in new_pocket:
                    new_pocket[key] += 1
                else:
                    new_pocket[key] = 1
    if neighbors == 2 or neighbors == 3:
        new_pocket[key_pos(x, y, z)] = active

def remove_invalid(new_pocket):
    to_remove = []
    for key, value in new_pocket.items():
        if (value != 3):
            to_remove.append(key)
    for key in to_remove:
        new_pocket.pop(key, None)

def pretty_print(cycle, new_pocket):
    print("After {} cycle(s):".format(cycle + 1))
    to_remove = []
    for key, value in new_pocket.items():
        if (value == 3):
            print(key, value)
        else:
            to_remove.append(key)
    for key in to_remove:
        new_pocket.pop(key, None)
    print('\n'*2)

def part2():
    pocket = parser()
    max_cycles = 6
    for cycle in range(max_cycles):
        new_pocket = {}
        for key, value in pocket.items():
            x, y, z, w = [int(number) for number in re.search("(.*) (.*) (.*) (.*)", key).groups()]
            rules_part2(x, y, z, w, pocket, new_pocket)
        remove_invalid(new_pocket)
        #pretty_print(cycle, new_pocket)
        pocket = new_pocket
    print(len(pocket))

def rules_part2(x, y, z, w, pocket, new_pocket):
    """
        - If a cube is active and exactly 2 or 3 of its neighbors are also active, the cube remains active.
        Otherwise, the cube becomes inactive.
        - If a cube is inactive but exactly 3 of its neighbors are active, the cube becomes active.
        Otherwise, the cube remains inactive.
    """
    neighbors = 0
    active = 3
    for comb in itertools.product([-1, 0, 1], repeat=4):
        new_x, new_y, new_z, new_w = x + comb[0], y + comb[1], z + comb[2], w + comb[3]
        if not comb == (0, 0, 0, 0):
            key = key_pos(new_x, new_y, new_z, new_w)
            if pocket.get(key, 0):
                neighbors += 1
            else:
                if key in new_pocket:
                    new_pocket[key] += 1
                else:
                    new_pocket[key] = 1
    if neighbors == 2 or neighbors == 3:
        new_pocket[key_pos(x, y, z, w)] = active

if __name__ == '__main__':
    part1()
    part2()