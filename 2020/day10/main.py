def part1():
    output_voltage = parser()
    adapter_rated = 3
    joltage = 0
    differences = {}
    count = 0
    while (count <= len(output_voltage)):
        count += 1
        for i in range(1, adapter_rated + 1):
            if (find_adapter(joltage + i, output_voltage)):
                joltage += i
                add_difference(differences, i)
                break
    # device's built-in adapter is always 3 higher than the highest adapter
    add_highest(differences)
    print(differences[1] * differences[3])

def find_adapter(joltage, output_voltage):
    return joltage in output_voltage

def add_difference(differences, joltage):
    if joltage in differences:
        differences[joltage] += 1
    else:
        differences[joltage] = 1

def add_highest(differences):
    differences[3] += 1

def parser():
    file = open("data.txt", "r")
    lines = file.readlines()
    data = []
    for line in lines:
        data.append(int(line))
    return data


def part2():
    output_voltage = parser()
    adapter_rated = 3
    res = 1
    output_cut = cut_output(output_voltage, adapter_rated)
    for output in output_cut:
        res *= recursive(output, adapter_rated, output[0])
    print(res)

def cut_output(data, adapter_rated):
    """
        Need to cut the file into subproblems for performance reasons.
    """
    output = []
    # don't forget to add the 0!
    data.append(0)
    data.sort()
    start = 0
    for end in range(len(data)):
        count = 0
        for i in range(1, 4):
            if (find_adapter(data[end] + i, data)):
                count += 1
        # data[j + 1] is an obligatory adapter and so a cut
        if count == 1:
            cut_index = end + 1
            # has more than 1 possibility of combination
            if cut_index - start >= 2:
                output.append(data[start:cut_index + 1])
            start = cut_index
    return output

def recursive(output_voltage, adapter_rated, joltage, res=1):
    first_find = True
    for i in range(1, adapter_rated + 1):
        is_find = find_adapter(joltage + i, output_voltage)
        if (is_find):
            if first_find:
                first_find = False
            else:
                res += 1
            res = recursive(output_voltage, adapter_rated, joltage + i, res)
    return res


if __name__ == '__main__':
    part1()
    part2()