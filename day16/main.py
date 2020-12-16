import re

def parser_part1():
    file = open("data.txt", "r")
    lines = file.readlines()
    fields = []
    tickets = []
    part_id = 1
    for line in lines:
        if line == "\n":
            part_id += 1
        else:
            if part_id == 1:
                res = re.search(": (.*) or (.*)$", line)
                cond1 = res.groups()[0]
                cond2 = res.groups()[1]
                fields.append(cond1.split("-"))
                fields.append(cond2.split("-"))
            elif part_id == 2:
                pass
            else:
                tickets += line.strip().split(',')
    return fields, tickets[1:]

def part1():
    fields, tickets = parser_part1()
    invalid = []
    for ticket in tickets:
        is_invalid = True
        for cond in fields:
            if int(cond[0]) <= int(ticket) <= int(cond[1]):
                is_invalid = False
                break
        if is_invalid:
            invalid.append(int(ticket))
    print(sum(invalid))


def part2():
    pass

if __name__ == "__main__":
    part1()
    part2()