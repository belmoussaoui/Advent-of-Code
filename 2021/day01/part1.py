
file = open("input.txt", "r")
lines = file.read().splitlines()

res = 0
for i in range(1, len(lines)):
    if (int(lines[i - 1]) < int(lines[i])):
        res += 1

print(res)
