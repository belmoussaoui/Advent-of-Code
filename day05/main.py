import re

def part1():
    file = open("data.txt", "r")
    lines = file.readlines()
    res = 0
    for line in lines:
        r_in = [0, 128]
        c_in = [0, 8]
        for i in range(7):
            sym = line[i]
            if (sym == 'B'):
                r_in[0] += max((r_in[1] - r_in[0]) / 2, 1)
            else:
                r_in[1] -= max((r_in[1] - r_in[0]) / 2, 1)
        for i in range(7, 10):
            sym = line[i]
            if (sym == 'R'):
                c_in[0] += max((c_in[1] - c_in[0]) / 2, 1)
            else:
                c_in[1] -= max((c_in[1] - c_in[0]) / 2, 1)
        row = int(r_in[1] if (line[7] == 'B') else r_in[0])
        column = int(c_in[1] if (line[7] == 'B') else c_in[0])
        seat_id = row * 8 + column
        if (res < seat_id):
            res = seat_id
    print(res)

def part2():
    file = open("data.txt", "r")
    lines = file.readlines()
    res = 0
    seats = [i * 8 + j for i in range(128) for j in range(8)]
    for line in lines:
        r_in = [0, 128]
        c_in = [0, 8]
        for i in range(7):
            sym = line[i]
            if (sym == 'B'):
                r_in[0] += max((r_in[1] - r_in[0]) / 2, 1)
            else:
                r_in[1] -= max((r_in[1] - r_in[0]) / 2, 1)
        for i in range(7, 10):
            sym = line[i]
            if (sym == 'R'):
                c_in[0] += max((c_in[1] - c_in[0]) / 2, 1)
            else:
                c_in[1] -= max((c_in[1] - c_in[0]) / 2, 1)
        row = int(r_in[1] if (line[7] == 'B') else r_in[0])
        column = int(c_in[1] if (line[7] == 'B') else c_in[0])
        seat_id = row * 8 + column
        seats.remove(seat_id)
    for i in range(len(seats)):
        if i != seats[i]:
            res = seats[i]
            break
    print(res)


if __name__ == '__main__':
    #part1()
    part2()