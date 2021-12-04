
file = open("input.txt", "r")
lines = file.read().splitlines()
measurements = list(map(int, lines))

def sum_3(m, i):
    return m[i] + m[i + 1] + m[i + 2]

res = 0
for i in range(0, len(lines) - 3):
    if (sum_3(measurements, i) < sum_3(measurements, i + 1)):
        res += 1

print(res)