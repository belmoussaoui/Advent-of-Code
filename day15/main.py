def parser():
    file = open("data.txt", "r")
    lines = file.readlines()
    data = lines[0].rstrip().split(",")
    return [int(elem) for elem in data]

def part1():
    numbers = parser()
    end = 2020
    turn = len(numbers) 
    while (turn != end):
        l_index = last_index(numbers[:-1], numbers[turn-1])
        if l_index == 0:
            value = 0
        else:
            value = turn - l_index
        numbers.append(value)
        turn += 1
    print(numbers[-1])

def last_index(l, i):
    if i in l:
        return ((len(l) - 1) - l[::-1].index(i)) + 1
    return 0


# use dic instead list to gain a lot of time :-)
# alway choose the best abstract data type
def part2():
    numbers = parser()
    end = 30000000
    dic = {numbers[i-1]: i for i in range(1, len(numbers))}
    current = dic.get(numbers[-1], 0)
    dic[numbers[-1]] = len(numbers)
    for turn in range(len(numbers), end-1):
        value = dic.get(current, 0)
        dic[current] = turn + 1
        if value == 0:
            current = 0
        else:
            current = (turn + 1) - value
    print(current)

if __name__ == "__main__":
    part1()
    part2()