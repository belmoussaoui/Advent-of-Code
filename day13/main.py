import math

def parser():
    file = open("data.txt", "r")
    lines = file.readlines()
    dic = {}
    dic["timestamp"] = int(lines[0])
    ids = lines[1].rstrip().split(",")
    dic["ids"] = [int(elem) if elem != "x" else 1 for elem in ids]
    return dic

def part1():
    data = parser()
    best = math.inf
    res = 0
    for i in data["ids"]:
        if i == 1:
            continue
        time = i - (data["timestamp"] % i)
        if (time == best and i < res):
            best = time
            res = i
        if (time < best):
            best = time
            res = i
    print(res * best)


# https://fr.wikipedia.org/wiki/Th%C3%A9or%C3%A8me_des_restes_chinois
def part2():
    data = parser()
    elem = [1] * len(data["ids"])
    prod = math.prod(data["ids"])
    res = 0
    for i in range(len(data["ids"])):
        bus_id = data["ids"][i]
        if bus_id == 1:
            continue
        n = int(prod / bus_id)
        v = 1
        while bus_id - ((n * v) % bus_id) != 1:
            v += 1
        elem[i] = n * v
    for i in range(len(elem)):
        if (elem[i] != 1): res += elem[i] * i
    res %= prod
    print(res)


if __name__ == "__main__":
    part1()
    part2()