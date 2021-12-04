operators = ["+", "*", "(", ")"]

def parser():
    file = open("data.txt", "r")
    lines = file.readlines()
    data = []
    indent = 0
    for line in lines:
        line = list(line.strip().replace(" ", ""))
        expression = []
        for elem in line:
            if elem not in operators:
                elem = int(elem)
            if elem == "(":
                indent_expression(expression, indent)
                indent += 1
            elif elem == ")":
                indent -= 1
            else:
                add_elem(expression, indent, elem)
        data.append(expression)
    return data

def indent_expression(expression, indent):
    if indent > 0:
        expression[-1].append([])
    else:
        expression.append([])

def add_elem(expression, indent, elem):
    if indent > 0:
        sub = expression
        for i in range(indent):
            sub = sub[-1]
        sub.append(elem)
    else:
        expression.append(elem)


def part1():
    homework = parser()
    res = 0
    for expression in homework:
        res += eval(eval_expression(expression))


def eval_expression(expression, res=0):
    global operators
    terms = []
    operator = ""
    for elem in expression:
        if isinstance(elem, list):
            new_result = eval_expression(elem)
            terms.append(new_result)
        elif not elem in operators:
            terms.append(str(elem))
        else:
            operator = elem
        if len(terms) == 2:
            res = eval(terms[0] + operator + terms[1])
            terms = [str(res)]
            operator = ""
    return terms[0]


def part2():
    homework = parser()
    res = 0
    for expression in homework:
        expression = paraddmul(expression)
        res += eval(eval_expression(expression))
    print(res)

def paraddmul(exp):
    res = []
    indent = 0
    i = 0
    for elem in exp:
        if (i < len(exp)):
            elem = exp[i]
            if elem == '+':
                last = res.pop()
                res.append([last, elem, exp[i + 1]])
                i += 1
            else:
                res.append(elem)
            i += 1
    return res

def paraddmul(exp):
    res = []
    indent = 0
    i = 0
    while i < len(exp):
        elem = exp[i]
        if (i < len(exp)):
            if isinstance(elem, list):
                new_result = paraddmul(elem)
                res.append(new_result)
            elif elem == '+':
                last = res.pop()
                if isinstance(exp[i + 1], list):
                    new_result = paraddmul(exp[i + 1])
                    res.append([last, elem, new_result])
                else:
                    res.append([last, elem, exp[i + 1]])
                i += 1
            else:
                res.append(elem)
        i += 1

    return res



if __name__ == '__main__':
    #part1()
    part2()