def part1():
    file = open("data.txt", "r")
    lines = file.readlines()
    for elem1 in lines:
        for elem2 in lines:
            if int(elem1) + int(elem2) == 2020:
                print(int(elem1) * int(elem2))

def part2():
    file = open("data.txt", "r")
    lines = file.readlines()
    for elem1 in lines:
        for elem2 in lines:
            for elem3 in lines:
                if int(elem1) + int(elem2) + int(elem3) == 2020:
                    print(int(elem1) * int(elem2) * int(elem3))


if __name__ == '__main__':
    part1()
    part2()