import copy
import time

def parser():
    file = open("data.txt", "r")
    lines = file.readlines()
    data = []
    for line in lines:
        data.append(list(line.rstrip()))
    return data

def part1():
    seat_layout = parser()
    occupied_seats = -1
    while occupied_seats != count_occupied_seats(seat_layout):
        #pretty_print(seat_layout)
        occupied_seats = count_occupied_seats(seat_layout)
        copy_layout = copy.deepcopy(seat_layout)
        for y in range(len(copy_layout)):
            for x in range(len(copy_layout[0])):
                if (rule1(x, y, copy_layout)):
                    seat_layout[y][x] = "#"
                elif (rule2(x, y, copy_layout)):
                    seat_layout[y][x] = "L"
                else:
                    pass
    print(count_occupied_seats(seat_layout))

def count_occupied_seats(seat_layout):
    count = 0
    for row in seat_layout:
        count += row.count("#")
    return count

def rule1(x, y, seat_layout):
    return seat_layout[y][x] == 'L' and count_occupied_seats_adjacent(x, y, seat_layout) == 0

def rule2(x, y, seat_layout):
    return seat_layout[y][x] == '#' and count_occupied_seats_adjacent(x, y, seat_layout) >= 4

def count_occupied_seats_adjacent(x, y, seat_layout):
    count = 0
    for dy in range(-1, 2):
        for dx in range(-1, 2):
            new_x = x + dx
            new_y = y + dy
            if ((dx != 0 or dy != 0) and is_valid(new_x, new_y, seat_layout)):
                if (seat_layout[new_y][new_x] == '#'):
                    count += 1
    return count

def is_valid(x, y, seat_layout):
    return -1 < x < len(seat_layout[0]) and -1 < y < len(seat_layout)

def pretty_print(seat_layout):
    for row in seat_layout:
        print(row)
    print()


def part2():
    seat_layout = parser()
    occupied_seats = -1
    while occupied_seats != count_occupied_seats(seat_layout):
        #pretty_print(seat_layout)
        occupied_seats = count_occupied_seats(seat_layout)
        copy_layout = copy.deepcopy(seat_layout)
        for y in range(len(copy_layout)):
            for x in range(len(copy_layout[0])):
                if (rule1_part2(x, y, copy_layout)):
                    seat_layout[y][x] = "#"
                elif (rule2_part2(x, y, copy_layout)):
                    seat_layout[y][x] = "L"
                else:
                    pass
    print(count_occupied_seats(seat_layout))

def rule1_part2(x, y, seat_layout):
    return seat_layout[y][x] == 'L' and count_occupied_seats_adjacent_part2(x, y, seat_layout) == 0

def rule2_part2(x, y, seat_layout):
    return seat_layout[y][x] == '#' and count_occupied_seats_adjacent_part2(x, y, seat_layout) >= 5

def count_occupied_seats_adjacent_part2(x, y, seat_layout):
    count = 0
    for dy in range(-1, 2):
        for dx in range(-1, 2):
            if (dx != 0 or dy != 0):
                distance = 1
                while True:
                    new_x = x + dx * distance
                    new_y = y + dy * distance
                    if (is_valid(new_x, new_y, seat_layout)):
                        if (seat_layout[new_y][new_x] == '#'):
                            count += 1
                            break
                        if (seat_layout[new_y][new_x] == 'L'):
                            break
                    else:
                        break
                    distance += 1
    return count


if __name__ == "__main__":
    part1()
    part2()
