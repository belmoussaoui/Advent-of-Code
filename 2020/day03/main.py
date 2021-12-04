def part1():
    file = open("data.txt", "r")
    lines = file.readlines()
    x = 0
    res = 0
    for line in lines:
        if line[x] == '#':
            res += 1
        x = (x + 3) % (len(line) - 1)
    print(res)


def part2():
    file = open("data.txt", "r")
    lines = file.readlines()
    x_list = [0] * 5
    dx = [1, 3, 5, 7, 0.5]
    temp = [0] * 5
    res = 1
    y = 0
    for line in lines:
        for i in range(len(x_list)):
            if (i != 4 or y % 2 == 0): 
                if line[int(x_list[i])] == '#':
                    temp[i] += 1
            x_list[i] = (x_list[i] + dx[i]) % (len(line) - 1)
            y += 1
    for x in temp:
        res *= x
    print(res)


if __name__ == '__main__':
    part1()
    part2()