
map = []

with open('03/input','r') as f:
    lines = [line for line in f]
    for line in lines:
        temp = [l for l in line if l != '\n']
        map.append(temp)

slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]

outs = []

for slope in slopes:
    i = 0
    j = 0
    out = 0
    right = slope[0]
    down = slope[1]
    width = len(map[0])

    while i < len(map)-1:
        i += down
        j += right
        #print(i, j, len(map), '0' if map[i][j%width] == '.' else 'X')
        out += 0 if map[i][j%width] == '.' else 1

    outs.append(out)

result = 1
for o in outs:
    result *= o
print("Result:", result)