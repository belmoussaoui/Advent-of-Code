file = open("input.txt", "r")
lines = file.read().splitlines()

course = [line.split() for line in lines]

horizontal_pos = 0
depth = 0
aim = 0

for commands in course:
    key = commands[0]
    value = int(commands[1])
    if (key == "forward"):
        horizontal_pos += value
        depth += aim * value
    elif (key == "up"):
        aim -= value
    elif (key == "down"):
        aim += value
    else:
        pass

print(horizontal_pos, depth,  horizontal_pos * depth)