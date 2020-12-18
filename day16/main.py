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
                fields.append([cond1.split("-"), cond2.split("-")])
            elif part_id == 2:
                self_ticket = line.strip().split(',')
            else:
                tickets.append(line.strip().split(','))
    return fields, self_ticket, tickets[1:]

def part1():
    fields, self_ticket, list_tickets = parser_part1()
    invalid = []
    for tickets in list_tickets:
        for ticket in tickets:
            is_invalid = True
            for cond in fields:
                if int(cond[0][0]) <= int(ticket) <= int(cond[0][1]):
                    is_invalid = False
                    break
                if int(cond[1][0]) <= int(ticket) <= int(cond[1][1]):
                    is_invalid = False
                    break
            if is_invalid:
                invalid.append(int(ticket))
    print(sum(invalid))
    return invalid


def part2(invalid):
    fields, self_ticket, list_tickets = parser_part1()
    valid = [[i for i in range(len(self_ticket))] for j in range(len(self_ticket))]
    for tickets in list_tickets:
        ticket_id = 0
        for ticket in tickets:
            field_id = 0
            for cond in fields:
                if not int(ticket) in invalid:
                    if not (int(cond[0][0]) <= int(ticket) <= int(cond[0][1])):
                        if  not (int(cond[1][0]) <= int(ticket) <= int(cond[1][1])):
                            if field_id in valid[ticket_id]:
                                valid[ticket_id].remove(field_id)
                field_id += 1
            ticket_id += 1
    queue = []
    for elem in valid:
        if len(elem) == 1:
            queue.append(elem[0])
    while len(queue) > 0:
        field_id = queue.pop()
        for elem in valid:
            if field_id in elem:
                if (len(elem) > 1):
                    elem.remove(field_id)
                    if (len(elem) == 1):
                        queue.append(elem[0])
    res = 1
    for x in range(len(valid)):
        if (valid[x][0] < 6):
            res *= int(self_ticket[x])
    print(res)

if __name__ == "__main__":
    invalid = part1()
    part2(invalid)