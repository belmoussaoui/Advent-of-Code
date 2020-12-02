def part1():
    file = open("data.txt", "r")
    lines = file.readlines()
    res = 0
    for line in lines:
        elem = line.split()
        cond = elem[0].split('-')
        char = elem[1][0]
        password = elem[2]
        if (int(cond[0]) <= password.count(char) <= int(cond[1])):
            res += 1
    print(res)



def part2():
    file = open("data.txt", "r")
    lines = file.readlines()
    res = 0
    for line in lines:
        elem = line.split()
        cond = elem[0].split('-')
        pos1 = int(cond[0]) - 1
        pos2 = int(cond[1]) - 1
        char = elem[1][0]
        p = elem[2]
        if (p[pos1] == char and not p[pos2] == char or not p[pos1] == char and p[pos2] == char):
            res += 1
    print(res)


if __name__ == '__main__':
    part1()
    part2()