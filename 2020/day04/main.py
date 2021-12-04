import re

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
    file = open("data.txt", "r")
    lines = file.readlines()
    p = ""
    res = 0
    for line in lines:
        if line == '\n':
            d = convert(p)
            if check(d) and is_valid(d):
                res += 1
            p = ""
        else:
            p += line
    if check(convert(p)):
        res += 1
    print(res)


def is_valid(d):
    if not (1920 <= int(d["byr"]) <= 2002):
        return False
    if not (2010 <= int(d["iyr"]) <= 2020):
        return False
    if not (2020 <= int(d["eyr"]) <= 2030):
        return False
    h = re.search("(^\d+)(cm$|in$)", d["hgt"])
    if h and h.groups()[1] == "cm":
        if not (150 <= int(h.groups()[0]) <= 193):
            return False
    elif h and h.groups()[1] == "in":
        if not (59 <= int(h.groups()[0]) <= 76):
            return False
    else:
        return False
    if not re.search("^#(?:[0-9a-fA-F]{6})$", d["hcl"]):
        return False
    if not (d["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]):
        return False
    if not re.search("^\d{9}$", d["pid"]):
        return False
    return True

if __name__ == '__main__':
    #part1()
    part2()