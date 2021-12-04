import math
import itertools

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
    instructions = parser()
    res = {}
    length = 36
    mask = ""
    res = {}
    for instruction in instructions:
        if instruction.get("mask", False):
            mask = instruction["mask"]
            continue
        add = bin(instruction["add"])[2:].zfill(length)
        value = instruction["value"]
        result = ""
        for i in range(length):
            if mask[i] == "X":
                result += "X"
            elif mask[i] == "1":
                result += "1"
            else:
                result += add[i]
        combination(result, value, res)
    print(sum(res.values()))

def combination(result, value, res):
    index = [i for i in range(len(result)) if result[i] == "X"]
    combs = list(map(list, itertools.product([0, 1], repeat=len(index))))
    for comb in combs:
        current = result
        for i in range(len(index)):
            current = current.replace("X", str(comb[i]), 1)
        res[int(current, 2)] = value

if __name__ == "__main__":
    part1()
    part2()