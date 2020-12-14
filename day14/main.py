import math

def parser():
    file = open("data.txt", "r")
    lines = file.readlines()
    instructions = []
    for i in range(0, len(lines)):
        elem = lines[i]
        if elem.split("=")[0].strip() == "mask":
            mask = elem.split("=")[1].strip()
            instructions.append({"mask": mask})
        else:
            s, e = elem.find("[") + 1, elem.find("]")
            add = int(elem[s:e])
            value = int(elem.split("=")[1].strip())
            instructions.append({"add": add, "value": value})
    return instructions

def part1():
    instructions = parser()
    res = {}
    length = 36
    mask = ""
    for instruction in instructions:
        if instruction.get("mask", False):
            mask = instruction["mask"]
            continue
        add = instruction["add"]
        value = bin(instruction["value"])[2:].zfill(length)
        result = ""
        for i in range(length):
            if mask[i] == "X":
                result += value[i]
            else:
                result += mask[i]
        res[add] = int(result, 2)
    print(sum(res.values()))


def part2():
    pass


if __name__ == "__main__":
    part1()
    #part2()