import math

def parser():
    file = open("data.txt", "r")
    lines = file.readlines()
    data = []
    for line in lines:
        data.append(line.rstrip())
    return data

def part1():
    instructions = parser()
    x, y, d = 0, 0, 0
    for command in instructions:
        action = command[0]
        value = int(command[1:])

        if action == "F":
            action = "E" if d == 0 else "N" if d == 1 else "W" if d == 2 else "S"

        if action == "E":
            x += value
        elif action == "N":
            y -= value
        elif action == "W":
            x -= value
        elif action == "S":
            y += value
        else:
            pass

        if action == "R":
            d = (d - int(value / 90)) % 4
        elif action == "L":
            d = (d + int(value / 90)) % 4
        else:
            pass
    print(abs(x) + abs(y))


def part2():
    instructions = parser()
    x, y, d = 0, 0, 0
    waypoint = {"x": 10, "y": -1}
    for command in instructions:
        action = command[0]
        value = int(command[1:])

        if action == "F":
            x += waypoint["x"] * value
            y += waypoint["y"] * value

        if action == "E":
            waypoint["x"] += value
        elif action == "N":
            waypoint["y"] -= value
        elif action == "W":
            waypoint["x"] -= value
        elif action == "S":
            waypoint["y"] += value
        else:
            pass

        if action == "R":
            angle = (-value * math.pi / 180)
            rotate_waypoint(waypoint, angle)
        elif action == "L":
            angle = (value * math.pi / 180)
            rotate_waypoint(waypoint, angle)
        else:
            pass
    print(abs(x) + abs(y))

def rotate_waypoint(waypoint, angle):
    x, y = waypoint["x"], waypoint["y"]
    waypoint["x"] = round(x * math.cos(angle) + y * math.sin(angle))
    waypoint["y"] = round(-x * math.sin(angle) + y * math.cos(angle))

if __name__ == "__main__":
    part1()
    part2()
