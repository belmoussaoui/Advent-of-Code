def part1():
    file = open("data.txt", "r")
    lines = file.readlines()
    p = ""
    res = 0
    for line in lines:
        if line == '\n':
            if check(convert(p)):
                res += 1
            p = ""
        else:
            p += line
    if check(convert(p)):
        res += 1
    print(res)

def convert(p):
    obj = p[:-1].replace('\n', ' ').replace(':', ' ').split(' ')
    it = iter(obj)
    return dict(zip(it, it))

def check(d):
    return len(d.keys()) == 8 or (len(d.keys()) == 7 and not "cid" in d)


def part2():
    pass

if __name__ == '__main__':
    part1()
    #part2()