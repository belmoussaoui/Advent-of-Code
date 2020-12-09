def part1():
    data = parser()
    index = 0
    length = 25
    while (is_valid(data, index, length)):
        index += 1
    print(data[index + length])

def is_valid(d, index, length):
    seq = (index, index + length)
    for i in range(*seq):
        for j in range(*seq):
            if (i != j):
                if is_sum(d[index + length], d[i], d[j]):
                    return True
    return False

def is_sum(value, v1, v2):
    return value == v1 + v2


def parser():
    file = open("data.txt", "r")
    lines = file.readlines()
    data = []
    for line in lines:
        data.append(int(line))
    return data

def part2():
    data = parser()
    index = 0
    length = 25
    while (is_valid(data, index, length)):
        index += 1
    invalid = data[index + length]
    for i in range(index + length):
        for j in range(1, (index + length) - i):
            contigous_set = data[i:i+j]
            if sum(contigous_set) == invalid:
                print(min(contigous_set) + max(contigous_set))
                break


if __name__ == '__main__':
    #part1()
    part2()