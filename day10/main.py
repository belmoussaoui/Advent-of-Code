def part1():
    output_voltage = parser()
    adapter_rated = 3
    joltage = 0
    differences = {}
    count = 0
    while (count <= len(output_voltage)):
        count += 1
        for i in range(1, adapter_rated + 1):
            is_find = find_adapter(joltage + i, output_voltage)
            if (is_find):
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
    data = parser()
    pass


if __name__ == '__main__':
    part1()
    #part2()