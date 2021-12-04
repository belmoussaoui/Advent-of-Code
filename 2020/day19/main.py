import re
import sys

def parser():
    file = open("data.txt", "r")
    lines = file.readlines()
    rules = {}
    messages = []
    mode = "top"
    for line in lines:
        line = line.strip()
        if line == "":
            mode = "bottom"
        elif mode == "top":
            parser_top(line, rules)
        else:
            parser_bottom(line, messages)
    return rules, messages

def parser_top(line, rules):
    split = line.split(':')
    key = int(split[0])
    split = split[1].strip().replace('"', '').split('|')
    if len(split) == 1:
        if "a" in split or "b" in split:
            value = {"type":1, "value": split[0]}
        else:
            split[0] = split[0].split(" ")
            value = {"type":0, "value": split}
    else:
        split1 = split[0].strip().split(" ")
        split2 = split[1].strip().split(" ")
        value = {"type":0, "value": [split1, split2]}
    rules[key] = value

def parser_bottom(line, messages):
    messages.append(line)


def part1():
    rules, messages = parser()
    res = match_rule_part1(rules)
    count = 0
    for message in messages:
        if message in res:
            count += 1
    print(count)

def match_rule_part1(rules, rule_id=0, res=[""]):
    value = rules[rule_id]["value"]
    if rules[rule_id]["type"] == 1:
        return [value]
    else:
        if len(value) == 1:
            res = next_rule(rules, value[0], res)
        else:
            res1 = next_rule(rules, value[0], res)
            res2 = next_rule(rules, value[1], res)
            res = [] + res1 + res2
    return res

def next_rule(rules, value, res):
    for new_rule_id in value:
        new_res = []
        for sub_res in res:
            for sub_sol in match_rule_part1(rules, int(new_rule_id)):
                new_res.append(sub_res + sub_sol)
        res = new_res
    return res

def part2():
    # to do :-(
    pass

def match_rule_part2(rules, rule_id=0, res=[""]):
    value = rules[rule_id]["value"]
    if rules[rule_id]["type"] == 1:
        return [value]
    else:
        if len(value) == 1:
            res = next_rule_part2(rules, value[0], res, rule_id)
        else:
            res1 = next_rule_part2(rules, value[0], res, rule_id)
            res2 = next_rule_part2(rules, value[1], res, rule_id)
            res = [] + res1 + res2
    return res

def next_rule_part2(rules, value, res, rule_id):
    global loop
    for new_rule_id in value:

        # self loop!
        if rule_id and int(new_rule_id) == rule_id:
            for i in range(len(res)):
                res[i] += "{rule"+new_rule_id+"}"
            continue

        new_res = []
        for sub_res in res:
            for sub_sol in match_rule_part2(rules, int(new_rule_id)):
                new_res.append(sub_res + sub_sol)
        res = new_res
    return res

def fix_rules(rules):
    #rules[8]["value"] = [["42"], ["8"]]
    rules[11]["value"] = [["42", "31"], ["42", "11", "31"]]




if __name__ == '__main__':
    #part1()
    part2()