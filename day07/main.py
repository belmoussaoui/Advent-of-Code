def part1(bag):
    dic = parser()
    res = -1  # because don't count the bag of search
    for key in dic:
        queue = [key]
        while (len(queue) > 0):
            e = queue.pop()
            if (bag == e):
                res += 1
                break
            for val in dic[e]:
                if (len(val) > 0):
                    queue.append(val[0])
    print(res)

def parser():
    dic = {}
    file = open("data.txt", "r")
    lines = file.readlines()
    for line in lines:
        bags = [bag.strip() for bag in line.replace('contain', ',').split(',')]
        bags = [bag.split(' ') for bag in bags]
        key = '-'.join(bags[0][:-1])
        dic[key] = [];
        for elem in bags[1:]:
            if (elem[0] == 'no'):
                val = []
            else:
                val = ['-'.join(elem[1:3]), int(elem[0])]
            dic[key].append(val)
    return dic

def part2():
    file = open("data.txt", "r")
    lines = file.readlines()


if __name__ == '__main__':
    part1('shiny-gold')
    # part2()