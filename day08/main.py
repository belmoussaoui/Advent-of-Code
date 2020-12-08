def part1():
    global accumulator
    boot_code = parser()
    execute(boot_code)
    print(accumulator)

def execute(boot_code):
    global accumulator
    accumulator = 0
    index = 0
    visited = []
    while (not is_eof(boot_code, index) and not is_loop(index, visited)):
        # debug(index, accumulator)
        visited.append(index)
        command = boot_code[index][0]
        arg = int(boot_code[index][1])
        if (command == "acc"):
            index += 1
            accumulator += arg
        elif (command == "jmp"):
            index += arg
        else:
            index += 1
    return is_eof(boot_code, index)

def is_eof(boot_code, index):
    return len(boot_code) == index

def is_loop(index, visited):
    return index in visited

def debug(index, accumulator):
    print(index, accumulator)

def parser():
    file = open("data.txt", "r")
    lines = file.readlines()
    boot_code = []
    for line in lines:
        boot_code.append(line.rstrip().split(' '))
    return boot_code

def part2():
    global accumulator
    boot_code = parser()
    for instruction in boot_code:
        command = instruction[0]
        if (command == "nop"):
            instruction[0] = "jmp"
            if execute(boot_code):
                break
            instruction[0] = "nop"
        if (command == "jmp"):
            instruction[0] = "nop"
            if execute(boot_code):
                break
            instruction[0] = "jmp"
    print(accumulator)


if __name__ == '__main__':
    part1()
    part2()