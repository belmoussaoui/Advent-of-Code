def part1():
    file = open("data.txt", "r")
    lines = file.readlines()
    p = ""
    res = 0
    for line in lines:
        if line == '\n':
            res += len(set(p.replace('\n', '')))
            p = ""
        else:
            p += line
    res += len(set(p.replace('\n', '')))
   # print(res)


#https://stackoverflow.com/questions/57210753/find-common-values-in-multiple-lists
def part2():
    file = open("data.txt", "r")
    lines = file.readlines()
    p = ""
    res = 0
    for line in lines:
        if line == '\n' or line == lines[-1]:
            obj = [list(elem) for elem in p[:-1].split('\n')]
            res += len(list(set.intersection(*map(set, obj))))
            p = ""
        else:
            p += line
    obj = [list(elem) for elem in p[:-1].split('\n')]
    res += len(list(set.intersection(*map(set, obj))))
    print(res)


if __name__ == '__main__':
    part1()
    part2()